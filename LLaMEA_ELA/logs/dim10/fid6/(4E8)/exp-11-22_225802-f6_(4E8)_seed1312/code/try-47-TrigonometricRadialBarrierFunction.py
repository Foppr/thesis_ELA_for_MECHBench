import numpy as np

class TrigonometricRadialBarrierFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        normalized_x = x / 5.0
        
        # Radial component with trigonometric oscillations
        r = np.sqrt(np.sum(normalized_x**2))
        radial_term = np.sin(10 * np.pi * r) * np.exp(-r**2)
        
        # Angular component with multiple frequency harmonics
        angle_sum = 0.0
        for i in range(self.dim):
            angle_sum += np.sin((i + 1) * np.pi * normalized_x[i]) * np.cos((i + 1) * np.pi * normalized_x[i])
        
        # Combined radial-angular term
        result = radial_term * angle_sum
        
        # Add multiple local minima using periodic functions
        for i in range(self.dim):
            result += 0.5 * np.sin(5 * np.pi * normalized_x[i]) * np.cos(3 * np.pi * normalized_x[i])
            
        # Conditional penalty based on distance from origin
        penalty = 0.0
        if r < 0.3:
            penalty = 10.0 * (1.0 / (r + 1e-8) - 1.0)
        elif r > 0.7:
            penalty = 5.0 * (r - 0.7)**2
            
        result += penalty
        
        # Add high-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(20 * normalized_x[i]) * np.cos(15 * normalized_x[i])
            
        result += 0.1 * noise
        
        # Add cross-dimensional coupling with sine interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(np.pi * (normalized_x[i] + normalized_x[j])) * \
                          np.cos(2 * np.pi * (normalized_x[i] - normalized_x[j]))
                
        result += 0.3 * coupling
        
        # Add global scaling and shift to ensure proper conditioning
        result += 0.5 * np.sum(normalized_x**4)
        
        return result