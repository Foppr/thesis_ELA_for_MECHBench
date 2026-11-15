import numpy as np

class SaddleMountainBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with modified conditioning
        f1 = 0.3 * np.sum(x**2)
        
        # Multiple asymmetric Gaussian peaks with dynamic positions and heights
        peaks = []
        for i in range(6):
            mu = np.array([3.0 * np.sin(0.4 * i), 2.5 * np.cos(0.6 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.2 + 0.6 * np.sin(0.5 * i)
            height = 2.0 + 3.0 * np.cos(0.3 * i)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Enhanced saddle point structure with higher-order interactions
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += np.tanh(x[i]) * np.tanh(x[j]) * np.sin(2.0 * x[i] * x[j]) * np.cos(0.5 * x[i] + x[j])
        
        # Introduce enhanced gradient variation with fractional exponents and trigonometric modulation
        f4 = 0.0
        for i in range(self.dim):
            f4 += (np.abs(x[i])**1.7 + 0.3 * np.sin(3.0 * x[i])) * np.sin(2.0 * x[i])
        
        # Add complex asymmetric basin structure with multi-scale exponential decay
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.2 * (x[i] - 2.0)**2) * np.cos(0.8 * x[i]) * np.sin(0.3 * x[i]**2)
        
        # Add cross-terms with higher-order interactions and nonlinearity
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.4 * np.sin(x[i] + x[j]) * np.cos(0.7 * x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add a new component to increase multimodality and complexity with chaotic modulation
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.25 * np.sin(4.0 * x[i]) * np.cos(0.4 * x[i]**2) * np.tanh(x[i])
        
        # Add a new component to increase complexity with periodic modulation
        f8 = 0.0
        for i in range(self.dim):
            f8 += 0.15 * np.sin(0.7 * x[i]) * np.exp(-0.15 * x[i]**2) * np.cos(2.0 * x[i])
        
        # Add enhanced noise term to increase robustness
        noise = 0.03 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + noise