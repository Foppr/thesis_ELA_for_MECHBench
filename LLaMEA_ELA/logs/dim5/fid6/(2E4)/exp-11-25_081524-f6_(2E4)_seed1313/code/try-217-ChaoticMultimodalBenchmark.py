import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quadratic base with chaotic coefficient modulation
        quadratic = 0.0
        for i in range(self.dim):
            a = 1.8 + 0.7 * np.sin(0.6 * self.t + i * 0.4 + np.sin(self.t * 0.8))
            b = 1.2 + 0.6 * np.cos(0.7 * self.t + i * 0.5 + np.cos(self.t * 0.9))
            c = 0.4 + 0.3 * np.sin(0.8 * self.t + i * 0.6 + np.sin(self.t * 1.0))
            quadratic += a * x[i]**2 + b * x[i] + c
            
        # Enhanced trigonometric coupling with chaotic phase modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                phase = 0.9 * np.sin(0.8 * self.t + i * 0.5 + j * 0.4 + np.cos(self.t * 0.7))
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                trig_coupling += np.sin(dist + phase) * np.cos(dist - phase) * np.exp(-0.15 * dist)
                
        # Enhanced radial basis function with chaotic centers and widths
        rbf = 0.0
        num_centers = min(15, self.dim)
        for i in range(num_centers):
            center = -4.0 + 8.0 * (i / (num_centers - 1)) if num_centers > 1 else 0.0
            width = 0.2 + 0.5 * np.sin(0.6 * self.t + i * 0.4 + np.cos(self.t * 0.8))
            rbf += np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2) * (1.0 + 0.3 * np.sin(self.t + i * 0.6))
            
        # Enhanced chaotic penalty with dynamic thresholds
        penalty = 0.0
        for i in range(self.dim):
            dist_from_origin = np.abs(x[i])
            if dist_from_origin > 2.0:
                penalty += 10.0 * (dist_from_origin - 2.0)**2 + 3.0 * (dist_from_origin - 2.0)**3 + 0.7 * np.sin(self.t + i * 0.7)
                
        # Enhanced chaotic scaling factor with multiple time components
        scale_factor = 1.3 + 0.4 * np.sin(0.9 * self.t) + 0.3 * np.cos(1.0 * self.t) + 0.2 * np.sin(1.2 * self.t)
        
        # Enhanced chaotic component weights with time-varying amplitudes
        w1 = 0.3 + 0.2 * np.sin(0.7 * self.t + np.sin(self.t * 0.9))
        w2 = 0.4 + 0.25 * np.cos(0.8 * self.t + np.cos(self.t * 1.0))
        w3 = 0.2 + 0.15 * np.sin(0.9 * self.t + np.sin(self.t * 1.3))
        w4 = 0.1 + 0.05 * np.cos(1.0 * self.t + np.cos(self.t * 1.4))
        
        result = w1 * quadratic + w2 * trig_coupling + w3 * rbf + w4 * penalty
        result *= scale_factor
        
        return result