import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for greater complexity
        self.freq_params = 2.5 + 3.5 * np.sin(np.arange(dim) * 1.1)
        self.amp_params = 1.2 + 1.0 * np.cos(np.arange(dim) * 1.5)
        self.saddle_params = 0.6 + 0.9 * np.sin(np.arange(dim) * 0.7 + np.pi/6)
        self.chaos_params = 0.7 + 0.5 * np.sin(np.arange(dim) * 0.9 + np.pi/4)
        # Additional exponential coupling parameters
        self.exp_coupling = 0.5 + 0.4 * np.cos(np.arange(dim) * 1.0 + np.pi/3)
        # New higher-order polynomial weights and chaos modifiers
        self.poly_weights = 1.8 + 1.3 * np.sin(np.arange(dim) * 0.8 + np.pi/5)
        self.chaos_modifiers = 0.2 + 0.3 * np.cos(np.arange(dim) * 1.3 + np.pi/7)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis with chaotic width and exponential decay
        radial_basis = 0.0
        for i in range(self.dim):
            width = 1.8 + 0.5 * np.sin(i * 0.7 + self.chaos_params[i])
            radial_basis += np.exp(-0.35 * (x[i] / width)**2) * np.cos(0.25 * x[i]**2)
        
        # Complex trigonometric component with multi-frequency modulation
        trig_component = 0.0
        for i in range(self.dim):
            freq1 = self.freq_params[i]
            freq2 = 1.8 * freq1
            amp1 = self.amp_params[i]
            amp2 = 0.7 * amp1
            trig_component += amp1 * np.sin(freq1 * x[i] + 0.4 * np.cos(freq1 * x[i])) * \
                              np.cos(freq2 * x[i]**2 + 0.3 * np.sin(x[i]) + 0.15 * np.sin(freq1 * x[i]))
        
        # Enhanced asymmetric saddle point with chaotic perturbation
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_params[i] * (x[i]**5 - 4*x[i]**3 + 3*x[i]) * \
                           np.exp(-0.2 * x[i]**2 + 0.15 * np.sin(x[i]) + 0.08 * np.cos(x[i]))
        
        # Cross-dimensional interaction with exponential coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            coupling_strength = 1.3 + 0.6 * np.sin(i * 0.8 + self.chaos_params[i])
            cross_interaction += coupling_strength * np.sin(2.5 * x[i] + 0.6 * x[j] + 0.4 * np.cos(x[i])) * \
                                np.exp(-0.12 * (x[i] - x[j])**2 + 0.2 * np.sin(x[i] + x[j]) + 0.08 * np.cos(x[k]))
        
        # Novel mixed exponential and polynomial component with higher-order terms
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**5 + 3*x[i]**4 - 6*x[i]**3 + 2*x[i]**2 - x[i]) * \
                          np.exp(-0.12 * x[i]**2 + 0.2 * np.cos(x[i]) + 0.12 * np.sin(x[i]))
        
        # Chaotic polynomial with enhanced nonlinearities and higher-order terms
        chaotic_poly = 0.0
        for i in range(self.dim):
            chaotic_poly += (x[i]**6 + 0.8*x[i]**5 - 3*x[i]**4 + 1.2*x[i]**3 - x[i]**2 + 0.8*x[i]) * \
                            np.sin(0.4 * x[i] + self.chaos_params[i] + 0.3 * np.cos(x[i]))
        
        # Additional exponential interaction term with enhanced chaos
        exp_interaction = 0.0
        for i in range(self.dim):
            j = (i + 3) % self.dim
            exp_interaction += self.exp_coupling[i] * np.exp(-0.18 * (x[i] - x[j])**2) * \
                               np.sin(3.5 * x[i] + 0.8 * x[j] + 0.25 * np.cos(x[i]) + 0.08 * np.sin(x[j]))
        
        # Combine all components with new weights
        result = 0.12 * np.sum(x**2) + 0.32 * radial_basis + 0.23 * trig_component + \
                 0.16 * saddle_term + 0.10 * cross_interaction + 0.07 * mixed_term + \
                 0.05 * chaotic_poly + 0.06 * exp_interaction
        
        return result