import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with slight noise
        f_val = np.sum(x**2) + 0.01 * np.sum(np.random.rand(self.dim) * x**2)
        
        # Chaotic sinusoidal perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Asymmetric saddle points with polynomial interactions
        for i in range(self.dim):
            f_val += 0.2 * (x[i]**3) * np.sin(8 * x[i]) * np.cos(6 * x[i])
            
        # Dynamic global minimum structure with time-like dependency (via index)
        f_val += 0.15 * np.sum(np.sin(20 * x) * np.cos(15 * x) * np.sin(10 * x))
        
        # Add chaotic amplitude modulation using a logistic map-like component
        logistic_seq = np.array([1.0])
        for _ in range(self.dim):
            logistic_seq = np.append(logistic_seq, 3.9 * logistic_seq[-1] * (1 - logistic_seq[-1]))
        logistic_seq = logistic_seq[1:]
        
        f_val += 0.1 * np.sum(logistic_seq * np.sin(12 * x) * np.cos(9 * x) * x**2)
        
        # Add a complex high-order polynomial interaction term
        f_val += 0.05 * np.sum((x**5) * np.sin(4 * x) * np.cos(2 * x))
        
        return f_val