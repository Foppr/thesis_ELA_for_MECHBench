import numpy as np

class DynamicHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quadratic base with higher condition number and dynamic coupling
        quadratic = 0.0
        for i in range(self.dim):
            a = 1.0 + 2.0 * np.sin(0.4 * self.t + i * 0.3) * (1.0 + 0.5 * np.cos(0.6 * self.t + i * 0.4))
            b = 1.5 + 0.8 * np.cos(0.5 * self.t + i * 0.2)
            c = 0.3 + 0.2 * np.sin(0.7 * self.t + i * 0.5)
            quadratic += a * x[i]**2 + b * x[i] + c
            
        # Complex trigonometric coupling with higher frequency interactions
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                phase = 1.2 * np.sin(0.8 * self.t + i * 0.4 + j * 0.3) + 0.5 * np.cos(0.6 * self.t + i * 0.2 + j * 0.1)
                dist = np.sqrt((x[i] - x[j])**2 + 0.001)
                trig_coupling += 2.0 * np.sin(dist + phase) * np.cos(dist - phase) * np.exp(-0.1 * dist)
                
        # Modified radial basis function with multiple centers and time-varying topology
        rbf = 0.0
        num_centers = min(12, self.dim)
        for i in range(num_centers):
            center = -4.0 + 8.0 * (i / (num_centers - 1)) if num_centers > 1 else 0.0
            width = 0.2 + 0.3 * np.sin(0.5 * self.t + i * 0.3) * np.cos(0.4 * self.t + i * 0.2)
            rbf += np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2) * (1.0 + 0.3 * np.sin(0.8 * self.t + i * 0.1))
            
        # Enhanced penalty with multiple thresholds and non-polynomial scaling
        penalty = 0.0
        for i in range(self.dim):
            dist_from_origin = np.abs(x[i])
            if dist_from_origin > 2.5:
                penalty += 8.0 * (dist_from_origin - 2.5)**2.5 + 3.0 * (dist_from_origin - 2.5)**4
                
        # Dynamic scaling with chaotic behavior and dimension-dependent modulation
        scale_factor = 1.0 + 0.5 * np.sin(0.8 * self.t) * np.cos(0.6 * self.t) + 0.2 * np.log(self.dim + 1) * np.sin(0.9 * self.t)
        
        # Novel weight dynamics with chaotic modulation
        w1 = 0.3 + 0.15 * np.sin(0.6 * self.t + 0.5 * np.sin(0.8 * self.t))
        w2 = 0.4 + 0.2 * np.cos(0.7 * self.t + 0.3 * np.cos(0.9 * self.t))
        w3 = 0.15 + 0.1 * np.sin(0.5 * self.t + 0.4 * np.sin(0.7 * self.t))
        w4 = 0.15 + 0.1 * np.cos(0.6 * self.t + 0.2 * np.cos(0.8 * self.t))
        
        result = w1 * quadratic + w2 * trig_coupling + w3 * rbf + w4 * penalty
        result *= scale_factor
        
        return result