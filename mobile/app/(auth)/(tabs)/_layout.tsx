import AButton from '@/components/AButton'
import { TabBarIcon } from '@/components/navigation/TabBarIcon'
import { Tabs } from 'expo-router'

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: '#9AD14B',
        headerShown: false,
      }}
    >
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({
            color,
            focused,
          }: {
            color: string
            focused: boolean
          }) => (
            <TabBarIcon
              name={focused ? 'home' : 'home-outline'}
              color={color}
            />
          ),
        }}
      />
      <Tabs.Screen
        name="recipes"
        options={{
          title: 'Recipes',
          tabBarIcon: ({
            color,
            focused,
          }: {
            color: string
            focused: boolean
          }) => (
            <TabBarIcon
              name={focused ? 'food' : 'food-outline'}
              color={color}
            />
          ),
        }}
      />
      <Tabs.Screen
        name="account"
        options={{
          title: 'Account',
          tabBarIcon: ({
            color,
            focused,
          }: {
            color: string
            focused: boolean
          }) => (
            <TabBarIcon
              name={focused ? 'account' : 'account-outline'}
              color={color}
            />
          ),
        }}
      />
    </Tabs>
  )
}
