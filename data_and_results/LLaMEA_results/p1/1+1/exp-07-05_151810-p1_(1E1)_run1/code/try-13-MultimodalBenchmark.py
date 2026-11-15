import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with chaotic modulation and increased frequency
        freqs = np.arange(1, self.dim + 1) * np.pi / 1.2
        sinusoidal = np.sum(np.sin(freqs * x) * np.cos(freqs * x * 0.7) * np.exp(-0.2 * np.abs(x)))
        
        # Add cubic and quartic terms with cross-terms for increased complexity
        cubic = 0.2 * np.sum(x**3)
        quartic = 0.1 * np.sum(x**4)
        
        # Enhanced cross-terms between dimensions to create stronger interaction
        cross_term = 0.05 * np.sum(x[:-1] * x[1:] * np.sin(4.0 * x[:-1] + 3.0 * x[1:]))
        
        # Add a chaotic component with stronger nonlinearity and modified decay
        chaotic = 0.5 * np.sum(np.sin(np.exp(2.0 * x)) * np.cos(np.log(np.abs(x) + 1e-6)) * np.tanh(1.5 * x))
        
        # Add a new component with higher frequency oscillations and stronger coupling
        high_freq = np.sum(np.sin(20.0 * x) * np.cos(8.0 * x) * np.exp(-0.1 * x**2))
        
        # Add a new component with trigonometric coupling and exponential modulation
        trig_coupling = 0.25 * np.sum(np.sin(x) * np.cos(3.0 * x) * np.exp(-0.25 * np.abs(x)))
        
        # Add a new component with hyperbolic and exponential interactions
        hyperbolic = 0.15 * np.sum(np.tanh(x) * np.exp(-0.1 * x**2) * np.sin(2.5 * x))
        
        # Combine all components
        result = result + sinusoidal + cubic + quartic + cross_term + chaotic + high_freq + trig_coupling + hyperbolic
        
        return result