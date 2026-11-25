import numpy as np

class ExponentialTrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay rates and trigonometric frequencies with higher variability
        self.decay_rates = [0.02, 0.12, 0.22, 0.32, 0.42, 0.52, 0.62, 0.72, 0.82][:min(dim, 9)]
        self.frequencies = [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3][:min(dim, 9)]
        
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
            exponent = 1.0 + 1.2 * np.sin(i * 0.9)
            fractal += (np.abs(x[i])**exponent + np.abs(x[i+1])**exponent) * \
                      np.exp(-0.3 * (x[i]**2 + x[i+1]**2)) * \
                      np.cos(0.4 * (x[i] + x[i+1]))
        
        # Multi-scale trigonometric modulations with increased complexity
        multi_scale = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine multiple sine/cosine terms with varying amplitudes and phases
            multi_scale += (0.7 * np.sin(freq * x[i]) + 
                           0.5 * np.cos(2 * freq * x[i]) + 
                           0.4 * np.sin(3 * freq * x[i]) * np.cos(freq * x[i]) +
                           0.3 * np.cos(4 * freq * x[i]) * np.sin(2 * freq * x[i]) +
                           0.2 * np.sin(5 * freq * x[i]) * np.cos(3 * freq * x[i]))
        
        # Enhanced cross-dimensional exponential coupling with asymmetric interactions
        cross_coupling = 0.0
        for i in range(self.dim - 2):
            # Asymmetric coupling with stronger influence from earlier dimensions
            cross_coupling += (np.exp(-0.4 * x[i]**2) * np.exp(-0.5 * x[i+1]**2) * 
                              np.sin(1.0 * x[i] * x[i+1]) * 
                              (1 + 0.3 * np.cos(x[i+2])) * 
                              np.exp(-0.15 * (x[i] - x[i+1])**2))
        
        # Intensified valley-ridge compound with varying curvature and sharp transitions
        valley_ridge = 0.0
        for i in range(self.dim):
            # Create a combination of quadratic, quartic, and higher-order terms
            valley_ridge += (0.95 * x[i]**2 + 0.35 * x[i]**4 + 0.15 * x[i]**6 + 0.05 * x[i]**8) * \
                           np.exp(-0.2 * x[i]**2)
        
        # Augmented dimensional fractal coupling with recursive-like behavior
        recursive_coupling = 0.0
        for i in range(self.dim - 3):
            # Create a pattern that resembles recursive dimension scaling with higher complexity
            recursive_coupling += (np.sin(x[i]) * np.cos(x[i+1]) * 
                                 np.exp(-0.4 * (x[i+2]**2 + x[i+3]**2)) * 
                                 (1 + 0.6 * np.sin(2 * x[i] + x[i+1])) * 
                                 np.cos(0.5 * x[i] * x[i+2]))
        
        # Enhanced asymmetric exponential modulation with trigonometric components
        asym_mod = 0.0
        for i in range(self.dim):
            # Use more complex asymmetric exponential terms based on sign of variable
            if x[i] >= 0:
                asym_mod += np.exp(-0.5 * x[i]) * (np.sin(4 * x[i])**2 + 
                                                 np.cos(3 * x[i])**2) * \
                           np.cos(x[i])
            else:
                asym_mod += np.exp(-0.7 * np.abs(x[i])) * (np.cos(5 * x[i])**2 + 
                                                         np.sin(4 * x[i])**2) * \
                           np.sin(x[i])
        
        # Ultra-high-frequency oscillatory component with stronger exponential damping
        high_freq = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Add ultra-high-frequency sine and cosine components with strong exponential decay
            high_freq += (np.sin(20 * freq * x[i]) + np.cos(18 * freq * x[i])) * \
                        np.exp(-0.4 * np.abs(x[i]))
        
        # Enhanced multi-modal structure with deeper local minima and clustering
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima using complex trigonometric combinations
            multimodal += (np.sin(10 * x[i]) * np.cos(7 * x[i]) + 
                          0.8 * np.sin(12 * x[i]) * np.cos(8 * x[i]) + 
                          0.5 * np.sin(14 * x[i]) * np.cos(5 * x[i]) +
                          0.3 * np.sin(16 * x[i]) * np.cos(6 * x[i]) +
                          0.1 * np.sin(18 * x[i]) * np.cos(9 * x[i]))
        
        # Additional ruggedness through polynomial coupling with enhanced nonlinearity
        ruggedness = 0.0
        for i in range(self.dim - 1):
            ruggedness += (x[i]**5 + x[i+1]**5) * np.exp(-0.25 * (x[i] - x[i+1])**2) * \
                         np.sin(0.6 * (x[i] + x[i+1]))
        
        # Final combination with enhanced weights for increased complexity
        return base + 2.5 * exp_trig + 2.0 * fractal + 1.8 * multi_scale + 1.5 * cross_coupling + \
               1.6 * valley_ridge + 1.2 * recursive_coupling + 1.1 * asym_mod + 2.0 * high_freq + \
               1.0 * multimodal + 0.8 * ruggedness