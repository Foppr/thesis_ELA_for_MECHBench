import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay and trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-0.1 * r) * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Trigonometric components with varying frequencies and amplitudes
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 1.5 * (i + 1)
            amp = 1.0 / (i + 1)**1.5
            trig_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Asymmetric cross-dimensional coupling with exponential weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.05 * (i + j))
                coupling_term += weight * np.sin(x[i] * x[j]) * np.cos(0.5 * x[i] + 0.3 * x[j])
        
        # Polynomial and logarithmic components for additional complexity
        poly_term = np.sum(x**4) * np.exp(-0.05 * r)
        log_term = np.sum(np.log(1.0 + np.abs(x))) * np.sin(0.2 * r)
        
        # Final combination with chaotic scaling
        result = radial_term + trig_sum + coupling_term + poly_term + log_term
        
        return result