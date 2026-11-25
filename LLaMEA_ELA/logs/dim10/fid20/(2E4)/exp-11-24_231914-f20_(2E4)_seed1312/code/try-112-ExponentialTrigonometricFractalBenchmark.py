import numpy as np

class ExponentialTrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay rates and trigonometric frequencies
        self.decay_rates = [0.15, 0.25, 0.35, 0.45, 0.55][:min(dim, 5)]
        self.frequencies = [1.2, 2.4, 3.6, 4.8, 6.0][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with improved scaling
        base = np.sum(x**2) / self.dim
        
        # Enhanced exponential decay interactions with trigonometric coupling
        exp_trig = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i % len(self.decay_rates)]
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine exponential decay with sine and cosine using enhanced coupling
            exp_trig += np.exp(-rate * np.abs(x[i])) * (np.sin(freq * x[i]) * np.cos(freq * x[i]) + 
                                                       0.3 * np.sin(2 * freq * x[i]) * np.cos(2 * freq * x[i]))
        
        # Improved fractal-like dimension scaling with variable exponents
        fractal = 0.0
        for i in range(self.dim - 1):
            # Use power-law scaling with dimension-dependent exponents and enhanced interaction
            exponent = 1.2 + 0.3 * np.sin(i * 0.7)
            fractal += (np.abs(x[i])**exponent + np.abs(x[i+1])**exponent) * \
                      np.exp(-0.15 * (x[i]**2 + x[i+1]**2)) * (1 + 0.2 * np.sin(i * 0.3))
        
        # Enhanced multi-scale trigonometric modulations with varying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine multiple sine/cosine terms with different amplitudes and phases
            multi_scale += (0.6 * np.sin(freq * x[i]) + 
                           0.4 * np.cos(2 * freq * x[i]) + 
                           0.3 * np.sin(3 * freq * x[i]) * np.cos(freq * x[i]) +
                           0.2 * np.cos(4 * freq * x[i]))
        
        # Enhanced cross-dimensional exponential coupling with asymmetric interactions
        cross_coupling = 0.0
        for i in range(self.dim - 2):
            # Asymmetric coupling where later dimensions have less influence and add phase shifts
            cross_coupling += (np.exp(-0.2 * x[i]**2) * np.exp(-0.3 * x[i+1]**2) * 
                              np.sin(0.5 * x[i] * x[i+1]) * 
                              (1 + 0.15 * np.cos(x[i+2])) * 
                              np.exp(-0.1 * np.abs(x[i] - x[i+1])))
        
        # Enhanced valley-ridge compound with varying curvature and additional terms
        valley_ridge = 0.0
        for i in range(self.dim):
            # Create a combination of quadratic and higher-order terms with enhanced nonlinearity
            valley_ridge += (0.7 * x[i]**2 + 0.3 * x[i]**4 + 0.1 * x[i]**6) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced dimensional fractal coupling with recursive-like behavior and improved scaling
        recursive_coupling = 0.0
        for i in range(self.dim - 3):
            # Create a pattern that resembles recursive dimension scaling with additional coupling terms
            recursive_coupling += (np.sin(x[i]) * np.cos(x[i+1]) * 
                                 np.exp(-0.2 * (x[i+2]**2 + x[i+3]**2)) * 
                                 (1 + 0.4 * np.sin(2 * x[i] + x[i+1])) * 
                                 np.exp(-0.05 * np.abs(x[i] - x[i+2])))
        
        # Enhanced asymmetric exponential modulation with trigonometric components
        asym_mod = 0.0
        for i in range(self.dim):
            # Use asymmetric exponential terms based on sign of variable with enhanced nonlinearity
            if x[i] >= 0:
                asym_mod += np.exp(-0.3 * x[i]) * (np.sin(2 * x[i]) * np.cos(x[i]) + 
                                                 0.5 * np.sin(3 * x[i]))
            else:
                asym_mod += np.exp(-0.5 * np.abs(x[i])) * (np.cos(3 * x[i]) * np.sin(x[i]) + 
                                                         0.4 * np.cos(2 * x[i]))
        
        # Enhanced high-frequency oscillatory component with exponential damping
        high_freq = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Add high-frequency sine and cosine components with enhanced decay and additional terms
            high_freq += (np.sin(12 * freq * x[i]) + np.cos(10 * freq * x[i]) + 
                         0.3 * np.sin(8 * freq * x[i]) * np.cos(6 * freq * x[i])) * \
                        np.exp(-0.25 * np.abs(x[i]))
        
        # Enhanced combined multi-modal structure with variable depth and improved complexity
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima using different trigonometric combinations with enhanced variety
            multimodal += (np.sin(6 * x[i]) * np.cos(4 * x[i]) + 
                          0.6 * np.sin(8 * x[i]) * np.cos(5 * x[i]) + 
                          0.4 * np.sin(10 * x[i]) * np.cos(3 * x[i]) +
                          0.2 * np.sin(12 * x[i]) * np.cos(2 * x[i]))
        
        # Enhanced additional ruggedness through polynomial coupling with improved scaling
        ruggedness = 0.0
        for i in range(self.dim - 1):
            ruggedness += (x[i]**3 + x[i+1]**3) * np.exp(-0.2 * (x[i] - x[i+1])**2) * \
                         (1 + 0.15 * np.sin(i * 0.5))
        
        # Final combination with carefully tuned weights for improved performance
        return base + 1.8 * exp_trig + 1.4 * fractal + 1.2 * multi_scale + 0.9 * cross_coupling + \
               1.0 * valley_ridge + 0.8 * recursive_coupling + 0.7 * asym_mod + 1.3 * high_freq + \
               0.6 * multimodal + 0.5 * ruggedness