import numpy as np

class ExponentialTrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Significantly increased complexity with more aggressive parameters
        self.decay_rates = [0.22, 0.48, 0.62, 0.78, 0.92][:min(dim, 5)]
        self.frequencies = [2.2, 4.8, 6.2, 7.8, 9.2][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term
        base = np.sum(x**2) / self.dim
        
        # Enhanced exponential decay interactions with trigonometric coupling
        exp_trig = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i % len(self.decay_rates)]
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine exponential decay with sine and cosine using enhanced coupling
            exp_trig += np.exp(-rate * np.abs(x[i])) * (np.sin(freq * x[i]) * np.cos(freq * x[i]) + 
                                                        0.55 * np.sin(2 * freq * x[i]) * np.cos(0.5 * freq * x[i]))
        
        # Improved fractal-like dimension scaling with varying exponents
        fractal = 0.0
        for i in range(self.dim - 1):
            # Use power-law scaling with dimension-dependent exponents and additional coupling
            exponent = 1.3 + 0.6 * np.sin(i * 0.8)
            fractal += (np.abs(x[i])**exponent + np.abs(x[i+1])**exponent) * \
                      np.exp(-0.28 * (x[i]**2 + x[i+1]**2)) * \
                      (1 + 0.35 * np.sin(0.4 * i))
        
        # Enhanced multi-scale trigonometric modulations with varying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine multiple sine/cosine terms with different amplitudes and phases
            multi_scale += (0.75 * np.sin(freq * x[i]) + 
                           0.65 * np.cos(2 * freq * x[i]) + 
                           0.55 * np.sin(3 * freq * x[i]) * np.cos(freq * x[i]) +
                           0.45 * np.sin(0.5 * freq * x[i]) * np.cos(1.5 * freq * x[i]))
        
        # Enhanced cross-dimensional exponential coupling with asymmetric interactions
        cross_coupling = 0.0
        for i in range(self.dim - 2):
            # Asymmetric coupling where later dimensions have less influence with enhanced modulation
            cross_coupling += (np.exp(-0.38 * x[i]**2) * np.exp(-0.42 * x[i+1]**2) * 
                              np.sin(0.75 * x[i] * x[i+1]) * 
                              (1 + 0.28 * np.cos(x[i+2])) * 
                              (1 + 0.22 * np.sin(0.55 * i)))
        
        # Enhanced valley-ridge compound with varying curvature
        valley_ridge = 0.0
        for i in range(self.dim):
            # Create a combination of quadratic and higher-order terms with enhanced nonlinearity
            valley_ridge += (1.05 * x[i]**2 + 0.55 * x[i]**4) * np.exp(-0.28 * x[i]**2)
        
        # Enhanced dimensional fractal coupling with recursive-like behavior
        recursive_coupling = 0.0
        for i in range(self.dim - 3):
            # Create a pattern that resembles recursive dimension scaling with enhanced complexity
            recursive_coupling += (np.sin(x[i]) * np.cos(x[i+1]) * 
                                 np.exp(-0.38 * (x[i+2]**2 + x[i+3]**2)) * 
                                 (1 + 0.55 * np.sin(2 * x[i] + x[i+1])) * 
                                 (1 + 0.22 * np.cos(0.55 * i)))
        
        # Enhanced asymmetric exponential modulation with trigonometric components
        asym_mod = 0.0
        for i in range(self.dim):
            # Use asymmetric exponential terms based on sign of variable with enhanced coupling
            if x[i] >= 0:
                asym_mod += np.exp(-0.48 * x[i]) * (np.sin(2 * x[i]) * np.cos(x[i]) + 
                                                   0.35 * np.sin(0.5 * x[i]))
            else:
                asym_mod += np.exp(-0.68 * np.abs(x[i])) * (np.cos(3 * x[i]) * np.sin(x[i]) + 
                                                           0.45 * np.cos(0.7 * x[i]))
        
        # Enhanced high-frequency oscillatory component with exponential damping
        high_freq = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Add high-frequency sine and cosine components with exponential decay and enhanced modulation
            high_freq += (np.sin(17 * freq * x[i]) + np.cos(15 * freq * x[i])) * \
                        np.exp(-0.38 * np.abs(x[i])) * \
                        (1 + 0.22 * np.sin(0.45 * i))
        
        # Enhanced combined multi-modal structure with variable depth
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima using different trigonometric combinations with enhanced complexity
            multimodal += (np.sin(7.2 * x[i]) * np.cos(4.8 * x[i]) + 
                          0.75 * np.sin(8.8 * x[i]) * np.cos(5.5 * x[i]) + 
                          0.55 * np.sin(10.5 * x[i]) * np.cos(3.8 * x[i]) +
                          0.35 * np.sin(7.8 * x[i]) * np.cos(6.7 * x[i]))
        
        # Enhanced additional ruggedness through polynomial coupling
        ruggedness = 0.0
        for i in range(self.dim - 1):
            ruggedness += (x[i]**3 + x[i+1]**3) * np.exp(-0.32 * (x[i] - x[i+1])**2) * \
                         (1 + 0.28 * np.sin(0.55 * i))
        
        # Final combination with carefully tuned weights for improved performance
        return base + 2.9 * exp_trig + 2.5 * fractal + 2.3 * multi_scale + 2.0 * cross_coupling + \
               2.1 * valley_ridge + 1.9 * recursive_coupling + 1.8 * asym_mod + 2.4 * high_freq + \
               1.7 * multimodal + 1.6 * ruggedness