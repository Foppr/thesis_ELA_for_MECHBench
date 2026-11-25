import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial base with higher-order terms and dynamic conditioning
        polynomial = np.sum(x_scaled**5) + 0.4 * np.sum(x_scaled**7) + 0.2 * np.sum(np.abs(x_scaled)**3)
        
        # Chaotic trigonometric components with irrational frequencies and varying amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.2 * np.sin(i * np.sqrt(2)))
            amplitude = 1.0 / (1.0 + 0.5 * i**1.5)
            trigonometric += amplitude * np.cos(freq * x_scaled[i]) * np.sin(freq * x_scaled[i] + i * np.pi / 4)
        
        # Exponentially amplified cross-terms with chaotic phase shifts
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.6 * (x_scaled[i]**2 + x_scaled[j]**2))
                phase_shift = np.sin(7 * x_scaled[i] * x_scaled[j]) * np.cos(5 * x_scaled[i] * x_scaled[j])
                exponential += exp_term * phase_shift
        
        # Stronger non-separable interaction terms with cubic and quartic components
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_scaled[i]**4 + x_scaled[j]**4) * np.sin(4 * x_scaled[i] * x_scaled[j]) + \
                              (x_scaled[i]**2 * x_scaled[j]**2) * np.cos(2 * x_scaled[i] * x_scaled[j])
        
        # Additional high-order terms for increased complexity and chaotic behavior
        quadratic = 0.8 * np.sum(x_scaled**2)
        cubic = 0.25 * np.sum(x_scaled**3)
        quartic = 0.1 * np.sum(x_scaled**4)
        
        # Global scaling and combination with enhanced weight adjustments
        return 5.2 * polynomial + 3.5 * trigonometric + 2.8 * exponential + 2.2 * interaction + 1.2 * quadratic + 0.5 * cubic + 0.2 * quartic