import numpy as np

class DynamicHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base component with time-varying coefficients
        quadratic = 0.0
        for i in range(self.dim):
            a = 1.0 + 0.5 * np.sin(0.3 * self.t + i * 0.2)
            b = 0.8 + 0.3 * np.cos(0.4 * self.t + i * 0.3)
            c = 0.2 + 0.1 * np.sin(0.5 * self.t + i * 0.4)
            quadratic += a * x[i]**2 + b * x[i] + c
            
        # Trigonometric coupling with phase modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                phase = 0.5 * np.sin(0.6 * self.t + i * 0.3 + j * 0.2)
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                trig_coupling += np.sin(dist + phase) * np.cos(dist - phase)
                
        # Radial basis function with dynamic centers and widths
        rbf = 0.0
        num_centers = min(8, self.dim)
        for i in range(num_centers):
            center = -4.0 + 8.0 * (i / (num_centers - 1)) if num_centers > 1 else 0.0
            width = 0.5 + 0.3 * np.sin(0.4 * self.t + i * 0.2)
            rbf += np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Time-varying penalty based on distance from origin
        penalty = 0.0
        for i in range(self.dim):
            dist_from_origin = np.abs(x[i])
            if dist_from_origin > 3.0:
                penalty += 5.0 * (dist_from_origin - 3.0)**2 + 1.5 * (dist_from_origin - 3.0)**3
                
        # Dynamic scaling factor based on time and dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(0.7 * self.t) + 0.1 * np.log(self.dim + 1)
        
        # Combine components with adaptive weights
        w1 = 0.3 + 0.1 * np.sin(0.5 * self.t)
        w2 = 0.4 + 0.15 * np.cos(0.6 * self.t)
        w3 = 0.2 + 0.05 * np.sin(0.8 * self.t)
        w4 = 0.1 + 0.05 * np.cos(0.9 * self.t)
        
        result = w1 * quadratic + w2 * trig_coupling + w3 * rbf + w4 * penalty
        result *= scale_factor
        
        return result