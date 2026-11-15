import numpy as np

class SaddleMountainBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Add multiple asymmetric Gaussian peaks with varying heights and widths
        peaks = []
        for i in range(5):
            mu = np.array([2.5 * np.sin(0.6 * i), 3.5 * np.cos(0.4 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.2 + 0.5 * np.sin(0.8 * i)
            height = 1.0 + 2.5 * np.cos(0.5 * i)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Add saddle point structure with hyperbolic tangent modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += np.tanh(x[i]) * np.tanh(x[j]) * np.cos(1.2 * x[i] * x[j])
        
        # Introduce gradient variation through fractional exponents
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.abs(x[i])**1.7 * np.cos(2.0 * x[i])
        
        # Add asymmetric basin structure with exponential decay and cosine modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(0.7 * x[i])
        
        # Add cross-terms to increase interaction complexity
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.25 * np.cos(x[i] + x[j]) * np.sin(0.6 * x[i] * x[j])
        
        # Add noise term to increase robustness
        noise = 0.03 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise