import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic exponential components with fractional powers and dynamic phase shifts
        exp_terms = 0
        for i in range(self.dim):
            exp_terms += np.exp(-0.5 * np.abs(x[i])**1.7) * np.sin(2.5 * np.pi * x[i] + 0.3 * i)**3
        
        # Nested trigonometric modulations with varying frequencies and amplitude envelopes
        trig_modulation = 0
        for i in range(self.dim):
            trig_modulation += (1 + 0.3 * np.sin(0.7 * x[i])) * \
                              np.cos(5 * x[i] + 0.2 * i) * \
                              np.sin(3 * x[i] + 0.4 * i) * \
                              np.exp(-0.1 * x[i]**2)
            
        # Composite cross-dimensional interactions with polynomial coupling and chaotic coupling strengths
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.sin(0.3 * (i + j))**2 + 0.5
                cross_terms += coupling_strength * \
                              np.exp(-0.3 * (x[i]**2 + x[j]**2)) * \
                              np.sin(x[i] * x[j] + 0.1 * i * j) * \
                              np.cos(x[i] + x[j] + 0.2 * (i - j))
                
        # Multi-scale penalty landscape with fractal-like local minima and irregular basin boundaries
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 20 * (1 - np.exp(-0.03 * (dist_from_origin - 2.5)**2)) * \
                      np.sin(4 * np.pi * dist_from_origin)**3 + \
                      8 * np.exp(-0.15 * (dist_from_origin - 1.2)**2) * \
                      np.cos(5 * np.pi * dist_from_origin)**3 + \
                      5 * np.sin(7 * x[i])**2 * np.cos(3 * x[i])**2
        
        # Add global scaling and combine all components with chaotic weighting
        return 1.2 * (exp_terms + trig_modulation + cross_terms + penalty)