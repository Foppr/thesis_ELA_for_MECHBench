import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for greater complexity
        self.freq_params = 4.0 + 5.0 * np.sin(np.arange(dim) * 1.2)
        self.amp_params = 2.0 + 1.8 * np.cos(np.arange(dim) * 1.7)
        self.saddle_params = 1.0 + 1.5 * np.sin(np.arange(dim) * 0.8 + np.pi/5)
        self.chaos_params = 1.0 + 0.8 * np.sin(np.arange(dim) * 1.1 + np.pi/3)
        # Additional exponential coupling parameters
        self.exp_coupling = 0.8 + 0.7 * np.cos(np.arange(dim) * 1.2 + np.pi/4)
        # New higher-order polynomial weights and chaos modifiers
        self.poly_weights = 3.0 + 2.0 * np.sin(np.arange(dim) * 0.9 + np.pi/6)
        self.chaos_modifiers = 0.5 + 0.5 * np.cos(np.arange(dim) * 1.4 + np.pi/8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis with chaotic width and exponential decay
        radial_basis = 0.0
        for i in range(self.dim):
            width = 2.5 + 0.8 * np.sin(i * 0.8 + self.chaos_params[i])
            radial_basis += np.exp(-0.5 * (x[i] / width)**2) * np.cos(0.4 * x[i]**2)
        
        # Complex trigonometric component with multi-frequency modulation
        trig_component = 0.0
        for i in range(self.dim):
            freq1 = self.freq_params[i]
            freq2 = 2.5 * freq1
            amp1 = self.amp_params[i]
            amp2 = 0.9 * amp1
            trig_component += amp1 * np.sin(freq1 * x[i] + 0.6 * np.cos(freq1 * x[i])) * \
                              np.cos(freq2 * x[i]**2 + 0.5 * np.sin(x[i]) + 0.3 * np.sin(freq1 * x[i]))
        
        # Enhanced asymmetric saddle point with chaotic perturbation
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_params[i] * (x[i]**5 - 5*x[i]**3 + 4*x[i]) * \
                           np.exp(-0.3 * x[i]**2 + 0.3 * np.sin(x[i]) + 0.15 * np.cos(x[i]))
        
        # Cross-dimensional interaction with exponential coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            coupling_strength = 2.0 + 0.9 * np.sin(i * 0.9 + self.chaos_params[i])
            cross_interaction += coupling_strength * np.sin(4.0 * x[i] + 0.8 * x[j] + 0.6 * np.cos(x[i])) * \
                                np.exp(-0.2 * (x[i] - x[j])**2 + 0.3 * np.sin(x[i] + x[j]) + 0.15 * np.cos(x[k]))
        
        # Novel mixed exponential and polynomial component with higher-order terms
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**7 + 5*x[i]**6 - 10*x[i]**5 + 4*x[i]**4 - 2*x[i]**3 + x[i]**2 + 3*x[i]) * \
                          np.exp(-0.2 * x[i]**2 + 0.3 * np.cos(x[i]) + 0.2 * np.sin(x[i]))
        
        # Chaotic polynomial with enhanced nonlinearities and higher-order terms
        chaotic_poly = 0.0
        for i in range(self.dim):
            chaotic_poly += (x[i]**8 + x[i]**7 - 5*x[i]**6 + 2*x[i]**5 - 3*x[i]**4 + 1.5*x[i]**3 - 1.8*x[i]**2 + 0.5*x[i]) * \
                            np.sin(0.6 * x[i] + self.chaos_params[i] + 0.5 * np.cos(x[i]))
        
        # Additional exponential interaction term with enhanced chaos
        exp_interaction = 0.0
        for i in range(self.dim):
            j = (i + 3) % self.dim
            exp_interaction += self.exp_coupling[i] * np.exp(-0.25 * (x[i] - x[j])**2) * \
                               np.sin(5.0 * x[i] + 1.0 * x[j] + 0.4 * np.cos(x[i]) + 0.15 * np.sin(x[j]))
        
        # Combine all components with new weights
        result = 0.2 * np.sum(x**2) + 0.4 * radial_basis + 0.3 * trig_component + \
                 0.2 * saddle_term + 0.15 * cross_interaction + 0.1 * mixed_term + \
                 0.08 * chaotic_poly + 0.07 * exp_interaction
        
        return result