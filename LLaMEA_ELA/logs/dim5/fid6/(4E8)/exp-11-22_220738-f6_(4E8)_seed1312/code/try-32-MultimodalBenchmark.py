import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with chaotic scaling
        f_val = np.sum(x**2) * (1.0 + 0.1 * np.sin(10.0 * np.sum(x**2)))
        
        # Chaotic oscillatory component with exponential decay
        for i in range(self.dim):
            f_val += 0.5 * np.sin(20.0 * x[i]) * np.exp(-0.1 * abs(x[i]))
            
        # Implicit constraint landscape with repulsion fields
        repulsion = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                repulsion += 1.0 / (1.0 + np.exp(5.0 * (dist - 2.0)))
        f_val += 0.3 * repulsion
        
        # Dynamic dimensional coupling with sine modulation
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += x[i] * x[i+1] * np.sin(0.5 * (x[i]**2 + x[i+1]**2))
        f_val += 0.2 * coupling
        
        # Multiple Gaussian peaks with dynamic positions and widths
        peak_count = min(5, self.dim // 2)
        for i in range(peak_count):
            idx = (i * 3) % self.dim
            if idx + 2 < self.dim:
                pos = np.array([x[idx], x[idx+1], x[idx+2]])
                center = np.array([1.0, -1.0, 0.5])
                width = 0.5 + 0.5 * np.sin(i)
                f_val += 0.4 * np.exp(-0.5 * np.sum(((pos - center) / width)**2))
                
        # Exponential barrier terms to encourage boundary exploration
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(2.0 * (5.0 - abs(x[i])))
        f_val += 0.1 * barrier
        
        return f_val