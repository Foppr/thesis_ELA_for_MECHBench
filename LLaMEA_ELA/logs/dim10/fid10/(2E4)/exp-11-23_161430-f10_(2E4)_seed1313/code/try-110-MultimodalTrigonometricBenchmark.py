import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for greater complexity
        self.freq_params = 2.0 + 3.0 * np.sin(np.arange(dim) * 0.9)
        self.amp_params = 1.0 + 0.8 * np.cos(np.arange(dim) * 1.2)
        self.saddle_params = 0.5 + 0.7 * np.sin(np.arange(dim) * 0.5 + np.pi/6)
        self.chaos_params = 0.6 + 0.4 * np.sin(np.arange(dim) * 0.7 + np.pi/4)
        # Additional exponential coupling parameters
        self.exp_coupling = 0.4 + 0.3 * np.cos(np.arange(dim) * 0.8 + np.pi/3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis with chaotic width and exponential decay
        radial_basis = 0.0
        for i in range(self.dim):
            width = 1.5 + 0.4 * np.sin(i * 0.5 + self.chaos_params[i])
            radial_basis += np.exp(-0.3 * (x[i] / width)**2) * np.cos(0.2 * x[i]**2)
        
        # Complex trigonometric component with multi-frequency modulation
        trig_component = 0.0
        for i in range(self.dim):
            freq1 = self.freq_params[i]
            freq2 = 1.5 * freq1
            amp1 = self.amp_params[i]
            amp2 = 0.7 * amp1
            trig_component += amp1 * np.sin(freq1 * x[i] + 0.4 * np.cos(freq1 * x[i])) * \
                              np.cos(freq2 * x[i]**2 + 0.3 * np.sin(x[i]) + 0.1 * np.sin(freq1 * x[i]))
        
        # Enhanced asymmetric saddle point with chaotic perturbation
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_params[i] * (x[i]**4 - 4*x[i]**2) * \
                           np.exp(-0.2 * x[i]**2 + 0.15 * np.sin(x[i]) + 0.05 * np.cos(x[i]))
        
        # Cross-dimensional interaction with exponential coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling_strength = 1.0 + 0.5 * np.sin(i * 0.6 + self.chaos_params[i])
            cross_interaction += coupling_strength * np.sin(2.5 * x[i] + 0.6 * x[j] + 0.4 * np.cos(x[i])) * \
                                np.exp(-0.1 * (x[i] - x[j])**2 + 0.2 * np.sin(x[i] + x[j]))
        
        # Novel mixed exponential and polynomial component
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**5 + 3*x[i]**4 - 6*x[i]**3 + 2*x[i]**2 - x[i]) * \
                          np.exp(-0.1 * x[i]**2 + 0.2 * np.cos(x[i]) + 0.1 * np.sin(x[i]))
        
        # Chaotic polynomial with enhanced nonlinearities
        chaotic_poly = 0.0
        for i in range(self.dim):
            chaotic_poly += (x[i]**6 + 0.7*x[i]**5 - 3*x[i]**4 + 1.2*x[i]**3 - 1.5*x[i]**2 + x[i]) * \
                            np.sin(0.4 * x[i] + self.chaos_params[i] + 0.3 * np.cos(x[i]))
        
        # Additional exponential interaction term
        exp_interaction = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            exp_interaction += self.exp_coupling[i] * np.exp(-0.15 * (x[i] - x[j])**2) * \
                               np.sin(3.0 * x[i] + 0.8 * x[j] + 0.2 * np.cos(x[i]))
        
        # Combine all components with new weights
        result = 0.12 * np.sum(x**2) + 0.32 * radial_basis + 0.22 * trig_component + \
                 0.15 * saddle_term + 0.09 * cross_interaction + 0.06 * mixed_term + \
                 0.04 * chaotic_poly + 0.05 * exp_interaction
        
        return result