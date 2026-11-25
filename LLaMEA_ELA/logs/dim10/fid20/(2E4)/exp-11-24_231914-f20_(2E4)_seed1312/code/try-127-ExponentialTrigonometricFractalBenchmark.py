import numpy as np

class ExponentialTrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly mutated decay rates and frequencies for increased complexity
        self.decay_rates = [0.03, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85][:min(dim, 9)]
        self.frequencies = [0.35, 1.35, 2.35, 3.35, 4.35, 5.35, 6.35, 7.35, 8.35][:min(dim, 9)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with enhanced quadratic component
        base = np.sum(x**2) / self.dim + 0.1 * np.sum(np.abs(x)) / self.dim
        
        # Exponential decay interactions with intensified trigonometric coupling
        exp_trig = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i % len(self.decay_rates)]
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine exponential decay with higher-order sine and cosine products
            exp_trig += np.exp(-rate * np.abs(x[i])) * (np.sin(freq * x[i])**4 + 
                                                       np.cos(freq * x[i])**4) * \
                       (np.sin(3 * freq * x[i]) + np.cos(3 * freq * x[i]))
        
        # Enhanced fractal-like dimension scaling with recursive patterns
        fractal = 0.0
        for i in range(self.dim - 1):
            # Use power-law scaling with dimension-dependent exponents and additional coupling
            exponent = 1.0 + 1.3 * np.sin(i * 0.95)
            fractal += (np.abs(x[i])**exponent + np.abs(x[i+1])**exponent) * \
                      np.exp(-0.35 * (x[i]**2 + x[i+1]**2)) * \
                      np.cos(0.45 * (x[i] + x[i+1]))
        
        # Multi-scale trigonometric modulations with increased complexity
        multi_scale = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine multiple sine/cosine terms with varying amplitudes and phases
            multi_scale += (0.75 * np.sin(freq * x[i]) + 
                           0.55 * np.cos(2 * freq * x[i]) + 
                           0.45 * np.sin(3 * freq * x[i]) * np.cos(freq * x[i]) +
                           0.35 * np.cos(4 * freq * x[i]) * np.sin(2 * freq * x[i]) +
                           0.25 * np.sin(5 * freq * x[i]) * np.cos(3 * freq * x[i]))
        
        # Enhanced cross-dimensional exponential coupling with asymmetric interactions
        cross_coupling = 0.0
        for i in range(self.dim - 2):
            # Asymmetric coupling with stronger influence from earlier dimensions
            cross_coupling += (np.exp(-0.45 * x[i]**2) * np.exp(-0.55 * x[i+1]**2) * 
                              np.sin(1.1 * x[i] * x[i+1]) * 
                              (1 + 0.35 * np.cos(x[i+2])) * 
                              np.exp(-0.18 * (x[i] - x[i+1])**2))
        
        # Intensified valley-ridge compound with varying curvature and sharp transitions
        valley_ridge = 0.0
        for i in range(self.dim):
            # Create a combination of quadratic, quartic, and higher-order terms
            valley_ridge += (0.98 * x[i]**2 + 0.4 * x[i]**4 + 0.2 * x[i]**6 + 0.08 * x[i]**8) * \
                           np.exp(-0.25 * x[i]**2)
        
        # Augmented dimensional fractal coupling with recursive-like behavior
        recursive_coupling = 0.0
        for i in range(self.dim - 3):
            # Create a pattern that resembles recursive dimension scaling with higher complexity
            recursive_coupling += (np.sin(x[i]) * np.cos(x[i+1]) * 
                                 np.exp(-0.45 * (x[i+2]**2 + x[i+3]**2)) * 
                                 (1 + 0.65 * np.sin(2 * x[i] + x[i+1])) * 
                                 np.cos(0.55 * x[i] * x[i+2]))
        
        # Enhanced asymmetric exponential modulation with trigonometric components
        asym_mod = 0.0
        for i in range(self.dim):
            # Use more complex asymmetric exponential terms based on sign of variable
            if x[i] >= 0:
                asym_mod += np.exp(-0.55 * x[i]) * (np.sin(4 * x[i])**2 + 
                                                 np.cos(3 * x[i])**2) * \
                           np.cos(x[i])
            else:
                asym_mod += np.exp(-0.75 * np.abs(x[i])) * (np.cos(5 * x[i])**2 + 
                                                         np.sin(4 * x[i])**2) * \
                           np.sin(x[i])
        
        # Ultra-high-frequency oscillatory component with stronger exponential damping
        high_freq = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Add ultra-high-frequency sine and cosine components with strong exponential decay
            high_freq += (np.sin(22 * freq * x[i]) + np.cos(20 * freq * x[i])) * \
                        np.exp(-0.45 * np.abs(x[i]))
        
        # Enhanced multi-modal structure with deeper local minima and clustering
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima using complex trigonometric combinations
            multimodal += (np.sin(11 * x[i]) * np.cos(8 * x[i]) + 
                          0.85 * np.sin(13 * x[i]) * np.cos(9 * x[i]) + 
                          0.55 * np.sin(15 * x[i]) * np.cos(6 * x[i]) +
                          0.35 * np.sin(17 * x[i]) * np.cos(7 * x[i]) +
                          0.15 * np.sin(19 * x[i]) * np.cos(10 * x[i]))
        
        # Additional ruggedness through polynomial coupling with enhanced nonlinearity
        ruggedness = 0.0
        for i in range(self.dim - 1):
            ruggedness += (x[i]**6 + x[i+1]**6) * np.exp(-0.3 * (x[i] - x[i+1])**2) * \
                         np.sin(0.65 * (x[i] + x[i+1]))
        
        # Final combination with enhanced weights for increased complexity
        return base + 2.7 * exp_trig + 2.2 * fractal + 1.9 * multi_scale + 1.6 * cross_coupling + \
               1.7 * valley_ridge + 1.3 * recursive_coupling + 1.2 * asym_mod + 2.2 * high_freq + \
               1.1 * multimodal + 0.9 * ruggedness