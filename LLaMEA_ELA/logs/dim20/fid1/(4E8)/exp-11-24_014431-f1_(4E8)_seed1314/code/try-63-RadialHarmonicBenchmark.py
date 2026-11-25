import numpy as np

class RadialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add radial basis function components with varying widths and centers
        for i in range(self.dim):
            # Enhanced radial basis with sharper peaks and wider decay
            f_val += 0.8 * np.exp(-0.15 * (x[i] - 1.5)**2) + 0.6 * np.exp(-0.25 * (x[i] + 2.5)**2)
        
        # Add multi-scale harmonic oscillations with increased frequency and amplitude
        for i in range(self.dim):
            f_val += 0.4 * np.sin(3 * np.pi * x[i]) + 0.3 * np.sin(6 * np.pi * x[i]) + \
                     0.2 * np.sin(12 * np.pi * x[i]) + 0.1 * np.sin(24 * np.pi * x[i])
        
        # Add cross-dimensional interactions with stronger and more varied coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger adaptive coupling with exponential decay
                coupling = 0.05 * (1 + np.cos(0.5 * (i - j))) * np.exp(-0.1 * abs(i - j))
                f_val += coupling * np.sin(x[i] + x[j]) * np.cos(0.7 * (x[i] - x[j]))
        
        # Add enhanced polynomial conditioning with higher-order terms
        f_val += 0.3 * np.sum(x**4) + 0.2 * np.sum(x**6) + 0.1 * np.sum(x**8)
        
        # Add complex interaction term with stronger harmonic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(4 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add global sinusoidal modulation with stronger frequency
        f_val += 0.2 * np.sin(0.7 * np.sum(x)) + 0.15 * np.cos(0.4 * np.sum(x)**2)
        
        # Add a new chaotic component for increased complexity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(5 * x[i]) * np.cos(3 * x[i])
        f_val += 0.1 * chaos_term
        
        return f_val