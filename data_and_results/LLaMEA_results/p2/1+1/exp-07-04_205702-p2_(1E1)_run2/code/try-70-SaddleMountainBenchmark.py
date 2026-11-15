import numpy as np

class SaddleMountainBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        f1 = 0.3 * np.sum(x**2) + 0.2 * np.sum(x**4)
        
        # Add chaotic Gaussian peaks with fractal-like distribution
        peaks = []
        for i in range(6):
            mu = np.array([3.0 * np.sin(0.8 * i), 2.5 * np.cos(0.6 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.2 + 0.5 * np.sin(0.9 * i)
            height = 2.0 + 3.0 * np.cos(0.5 * i)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Introduce chaotic saddle structure with logistic map modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += np.tanh(x[i]) * np.tanh(x[j]) * np.sin(2.0 * x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
        
        # Add dynamic gradient variation with fractional calculus inspired terms
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.abs(x[i])**1.7 * np.sin(3.0 * x[i]) + 0.1 * np.cos(1.2 * x[i])
        
        # Asymmetric basin with time-delayed exponential decay
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.2 * (x[i] - 2.0)**2) * np.cos(0.8 * x[i]) * np.sin(0.3 * x[i])
        
        # Cross-terms with dynamic coupling coefficients
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.4 * (i + j))
                f6 += coupling * np.sin(x[i] + x[j]) * np.cos(0.7 * x[i] * x[j])
        
        # Add chaotic noise with deterministic pseudo-random component
        noise = 0.03 * np.sin(np.sum(x)**2) + 0.02 * np.cos(np.prod(x))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise