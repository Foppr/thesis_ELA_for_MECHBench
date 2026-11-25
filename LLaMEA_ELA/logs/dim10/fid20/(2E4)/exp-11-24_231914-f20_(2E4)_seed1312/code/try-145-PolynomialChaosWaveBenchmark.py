import numpy as np

class PolynomialChaosWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced parameter set for increased complexity and ruggedness
        self.decay_rates = [0.03, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85][:min(dim, 9)]
        self.frequencies = [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3][:min(dim, 9)]
        self.stochastic_perturbations = np.random.uniform(0.8, 1.2, dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with enhanced quadratic and cubic components
        base = (np.sum(x**2) / self.dim + 
                0.15 * np.sum(np.abs(x)) / self.dim + 
                0.05 * np.sum(x**3) / self.dim)
        
        # Polynomial chaos interactions with stochastic perturbations
        chaos = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i % len(self.decay_rates)]
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine polynomial chaos with stochastic modulation
            chaos += (np.exp(-rate * np.abs(x[i])) * 
                     (np.sin(freq * x[i])**5 + np.cos(freq * x[i])**5) * 
                     self.stochastic_perturbations[i])
        
        # Enhanced trigonometric wave interference with multi-scale coupling
        wave_interference = 0.0
        for i in range(self.dim - 1):
            # Use complex wave interference patterns with varying amplitudes
            wave_interference += (np.sin(2 * self.frequencies[i % len(self.frequencies)] * x[i]) * 
                                np.cos(3 * self.frequencies[(i+1) % len(self.frequencies)] * x[i+1]) + 
                                0.7 * np.cos(4 * self.frequencies[i % len(self.frequencies)] * x[i]) * 
                                np.sin(5 * self.frequencies[(i+1) % len(self.frequencies)] * x[i+1]))
        
        # Fractal-like coupling with recursive dimension scaling
        fractal = 0.0
        for i in range(self.dim - 2):
            # Create fractal patterns using power-law scaling and recursive interactions
            exponent = 1.2 + 1.5 * np.sin(i * 0.8)
            fractal += (np.abs(x[i])**exponent + np.abs(x[i+1])**exponent + 
                       np.abs(x[i+2])**exponent) * \
                      np.exp(-0.4 * (x[i]**2 + x[i+1]**2 + x[i+2]**2)) * \
                      np.cos(0.5 * (x[i] + x[i+1] + x[i+2]))
        
        # Multi-scale trigonometric modulations with increased complexity
        multi_scale = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Combine multiple sine/cosine terms with varying amplitudes and phases
            multi_scale += (0.9 * np.sin(freq * x[i]) + 
                           0.7 * np.cos(2 * freq * x[i]) + 
                           0.6 * np.sin(3 * freq * x[i]) * np.cos(freq * x[i]) +
                           0.5 * np.cos(4 * freq * x[i]) * np.sin(2 * freq * x[i]) +
                           0.4 * np.sin(5 * freq * x[i]) * np.cos(3 * freq * x[i]) +
                           0.3 * np.cos(6 * freq * x[i]) * np.sin(4 * freq * x[i]))
        
        # Enhanced cross-dimensional exponential coupling with asymmetric interactions
        cross_coupling = 0.0
        for i in range(self.dim - 3):
            # Asymmetric coupling with stronger influence from earlier dimensions and stochastic perturbations
            cross_coupling += (np.exp(-0.3 * x[i]**2) * np.exp(-0.4 * x[i+1]**2) * 
                              np.sin(1.2 * x[i] * x[i+1]) * 
                              (1 + 0.4 * np.cos(x[i+2])) * 
                              np.exp(-0.2 * (x[i] - x[i+1])**2) * 
                              self.stochastic_perturbations[i])
        
        # Intensified valley-ridge compound with varying curvature and sharp transitions
        valley_ridge = 0.0
        for i in range(self.dim):
            # Create a combination of quadratic, quartic, and higher-order terms
            valley_ridge += (1.0 * x[i]**2 + 0.4 * x[i]**4 + 0.25 * x[i]**6 + 0.1 * x[i]**8) * \
                           np.exp(-0.25 * x[i]**2)
        
        # Augmented dimensional fractal coupling with recursive-like behavior
        recursive_coupling = 0.0
        for i in range(self.dim - 4):
            # Create a pattern that resembles recursive dimension scaling with higher complexity
            recursive_coupling += (np.sin(x[i]) * np.cos(x[i+1]) * 
                                 np.exp(-0.5 * (x[i+2]**2 + x[i+3]**2)) * 
                                 (1 + 0.7 * np.sin(2 * x[i] + x[i+1])) * 
                                 np.cos(0.6 * x[i] * x[i+2]) * 
                                 self.stochastic_perturbations[i])
        
        # Enhanced asymmetric exponential modulation with trigonometric components
        asym_mod = 0.0
        for i in range(self.dim):
            # Use more complex asymmetric exponential terms based on sign of variable with stochastic perturbations
            if x[i] >= 0:
                asym_mod += np.exp(-0.6 * x[i]) * (np.sin(5 * x[i])**2 + 
                                                 np.cos(4 * x[i])**2) * \
                           np.cos(x[i]) * self.stochastic_perturbations[i]
            else:
                asym_mod += np.exp(-0.8 * np.abs(x[i])) * (np.cos(6 * x[i])**2 + 
                                                         np.sin(5 * x[i])**2) * \
                           np.sin(x[i]) * self.stochastic_perturbations[i]
        
        # Ultra-high-frequency oscillatory component with stronger exponential damping
        high_freq = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            # Add ultra-high-frequency sine and cosine components with strong exponential decay
            high_freq += (np.sin(25 * freq * x[i]) + np.cos(23 * freq * x[i])) * \
                        np.exp(-0.45 * np.abs(x[i]))
        
        # Enhanced multi-modal structure with deeper local minima and clustering
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima using complex trigonometric combinations
            multimodal += (np.sin(15 * x[i]) * np.cos(12 * x[i]) + 
                          0.95 * np.sin(17 * x[i]) * np.cos(13 * x[i]) + 
                          0.7 * np.sin(19 * x[i]) * np.cos(11 * x[i]) +
                          0.5 * np.sin(21 * x[i]) * np.cos(14 * x[i]) +
                          0.3 * np.sin(23 * x[i]) * np.cos(15 * x[i]) +
                          0.1 * np.sin(25 * x[i]) * np.cos(16 * x[i]))
        
        # Additional ruggedness through polynomial coupling with enhanced nonlinearity
        ruggedness = 0.0
        for i in range(self.dim - 1):
            ruggedness += (x[i]**7 + x[i+1]**7) * np.exp(-0.4 * (x[i] - x[i+1])**2) * \
                         np.sin(0.8 * (x[i] + x[i+1]))
        
        # Final combination with enhanced weights for increased complexity
        return base + 3.2 * chaos + 2.8 * wave_interference + 2.5 * fractal + 2.2 * multi_scale + \
               1.9 * cross_coupling + 2.0 * valley_ridge + 1.6 * recursive_coupling + \
               1.5 * asym_mod + 2.6 * high_freq + 1.4 * multimodal + 1.2 * ruggedness