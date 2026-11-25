import numpy as np

class MultimodalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with oscillating barrier
        r = np.sqrt(np.sum(x**2))
        radial_barrier = np.exp(-0.1 * r) * np.sin(3.0 * r)
        
        # Trigonometric multimodal components
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += np.sin(x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional interaction with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
                
        # Polynomial barrier terms
        poly_barrier = np.sum(x**4) * np.exp(-0.02 * r)
        
        # Additional harmonic components with varying frequencies
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.5
            harmonic_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * (1.0 / (1.0 + x[i]**2))
            
        # Final multimodal combination
        result = radial_barrier + trig_sum + cross_term + poly_barrier + harmonic_sum
        
        return result