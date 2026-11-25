import numpy as np

class DynamicHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with chaotic coefficient modulation
        quadratic = 0.0
        for i in range(self.dim):
            a = 1.0 + 0.3 * np.sin(0.5 * self.t + i * 0.4 + np.sin(self.t * 0.7))
            b = 0.9 + 0.2 * np.cos(0.6 * self.t + i * 0.3 + np.cos(self.t * 0.8))
            c = 0.1 + 0.15 * np.sin(0.7 * self.t + i * 0.5 + np.sin(self.t * 0.9))
            quadratic += a * x[i]**2 + b * x[i] + c
            
        # Enhanced trigonometric coupling with chaotic phase modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                phase = 0.4 * np.sin(0.7 * self.t + i * 0.3 + j * 0.2 + np.cos(self.t * 0.6))
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                trig_coupling += np.sin(dist + phase) * np.cos(dist - phase) * (1.0 + 0.2 * np.sin(self.t + i + j))
                
        # Radial basis function with chaotic center movement and time-varying widths
        rbf = 0.0
        num_centers = min(6, self.dim)
        for i in range(num_centers):
            center = -4.5 + 9.0 * (i / (num_centers - 1)) if num_centers > 1 else 0.0
            width = 0.4 + 0.25 * np.sin(0.5 * self.t + i * 0.3 + np.cos(self.t * 0.7))
            rbf += np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Chaotic penalty with dynamic threshold and scaling
        penalty = 0.0
        for i in range(self.dim):
            dist_from_origin = np.abs(x[i])
            if dist_from_origin > 2.5:
                penalty += 3.0 * (dist_from_origin - 2.5)**2 + 0.8 * (dist_from_origin - 2.5)**3
            elif dist_from_origin > 4.0:
                penalty += 10.0 * np.sin(2.0 * self.t + i) * (dist_from_origin - 4.0)**2
                
        # Dynamic scaling factor with chaotic component
        scale_factor = 1.0 + 0.15 * np.sin(0.8 * self.t + np.cos(self.t * 0.9)) + 0.08 * np.log(self.dim + 1)
        
        # Adaptive weights with chaotic modulation
        w1 = 0.25 + 0.1 * np.sin(0.6 * self.t + np.cos(self.t * 0.8))
        w2 = 0.35 + 0.12 * np.cos(0.7 * self.t + np.sin(self.t * 0.9))
        w3 = 0.25 + 0.08 * np.sin(0.9 * self.t + np.cos(self.t * 0.7))
        w4 = 0.15 + 0.07 * np.cos(0.8 * self.t + np.sin(self.t * 0.6))
        
        result = w1 * quadratic + w2 * trig_coupling + w3 * rbf + w4 * penalty
        result *= scale_factor
        
        return result