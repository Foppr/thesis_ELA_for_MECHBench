import numpy as np

class ExponentialTrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay rates and trigonometric frequencies
        self.decay_rates = [0.1, 0.2, 0.3, 0.4, 0.5][:min(dim, 5)]
        self.frequencies = [1.0, 2.0, 3.0, 4.0, 5.0][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term
        base = np.sum(x**2) / self.dim
        
        # Exponential decay interactions with trigonometric coupling
        exp_trig = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i % len(self.decay_rates)]
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine exponential decay with sine and cosine
            exp_trig += np.exp(-rate * np.abs(x[i])) * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Fractal-like dimension scaling with varying exponents
        fractal = 0.0
        for i in range(self.dim - 1):
            # Use power-law scaling with dimension-dependent exponents
            exponent = 1.0 + 0.5 * np.sin(i * 0.5)
            fractal += (np.abs(x[i])**exponent + np.abs(x[i+1])**exponent) * \
                      np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Multi-scale trigonometric modulations with varying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine multiple sine/cosine terms with different amplitudes
            multi_scale += (0.5 * np.sin(freq * x[i]) + 
                           0.3 * np.cos(2 * freq * x[i]) + 
                           0.2 * np.sin(3 * freq * x[i]) * np.cos(freq * x[i]))
        
        # Cross-dimensional exponential coupling with asymmetric interactions
        cross_coupling = 0.0
        for i in range(self.dim - 2):
            # Asymmetric coupling where later dimensions have less influence
            cross_coupling += (np.exp(-0.2 * x[i]**2) * np.exp(-0.3 * x[i+1]**2) * 
                              np.sin(0.5 * x[i] * x[i+1]) * 
                              (1 + 0.1 * np.cos(x[i+2])))
        
        # Valley-ridge compound with varying curvature
        valley_ridge = 0.0
        for i in range(self.dim):
            # Create a combination of quadratic and higher-order terms
            valley_ridge += (0.8 * x[i]**2 + 0.2 * x[i]**4) * np.exp(-0.1 * x[i]**2)
        
        # Dimensional fractal coupling with recursive-like behavior
        recursive_coupling = 0.0
        for i in range(self.dim - 3):
            # Create a pattern that resembles recursive dimension scaling
            recursive_coupling += (np.sin(x[i]) * np.cos(x[i+1]) * 
                                 np.exp(-0.2 * (x[i+2]**2 + x[i+3]**2)) * 
                                 (1 + 0.3 * np.sin(2 * x[i] + x[i+1])))
        
        # Asymmetric exponential modulation with trigonometric components
        asym_mod = 0.0
        for i in range(self.dim):
            # Use asymmetric exponential terms based on sign of variable
            if x[i] >= 0:
                asym_mod += np.exp(-0.3 * x[i]) * np.sin(2 * x[i]) * np.cos(x[i])
            else:
                asym_mod += np.exp(-0.5 * np.abs(x[i])) * np.cos(3 * x[i]) * np.sin(x[i])
        
        # High-frequency oscillatory component with exponential damping
        high_freq = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Add high-frequency sine and cosine components with exponential decay
            high_freq += (np.sin(10 * freq * x[i]) + np.cos(8 * freq * x[i])) * \
                        np.exp(-0.2 * np.abs(x[i]))
        
        # Combined multi-modal structure with variable depth
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima using different trigonometric combinations
            multimodal += (np.sin(5 * x[i]) * np.cos(3 * x[i]) + 
                          0.5 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 
                          0.3 * np.sin(9 * x[i]) * np.cos(2 * x[i]))
        
        # Add additional ruggedness through polynomial coupling
        ruggedness = 0.0
        for i in range(self.dim - 1):
            ruggedness += (x[i]**3 + x[i+1]**3) * np.exp(-0.15 * (x[i] - x[i+1])**2)
        
        # Final combination with carefully tuned weights
        return base + 1.5 * exp_trig + 1.2 * fractal + 1.0 * multi_scale + 0.8 * cross_coupling + \
               0.9 * valley_ridge + 0.7 * recursive_coupling + 0.6 * asym_mod + 1.1 * high_freq + \
               0.5 * multimodal + 0.4 * ruggedness