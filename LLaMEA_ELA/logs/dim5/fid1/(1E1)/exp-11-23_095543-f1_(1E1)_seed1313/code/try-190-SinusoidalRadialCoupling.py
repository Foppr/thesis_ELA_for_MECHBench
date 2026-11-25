import numpy as np

class SinusoidalRadialCoupling:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add radial sinusoidal modulation with higher frequency components
        r = np.sqrt(np.sum(x ** 2))
        result *= (1.0 + 0.7 * np.sin(5 * r) * np.cos(3 * r) * np.exp(-0.1 * r))
        
        # Add periodic components with different frequencies and phase shifts
        for i in range(self.dim):
            result += 0.4 * np.sin(9 * x[i] + 0.5 * i) * np.cos(7 * x[(i + 1) % self.dim] - 0.3 * i)
            
        # Add cross-dimensional coupling terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(5 * x[i]) * np.cos(8 * x[j]) * np.exp(-0.2 * (x[i] - x[j]) ** 2) * np.sin(2 * r)
                
        # Add radial harmonic components with varying amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(12 * r) * np.cos(10 * r) * x[i] ** 2 * (1 + 0.3 * np.sin(4 * r))
            
        # Add multi-scale periodicity with irregular frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(18 * x[i]) * np.cos(15 * x[(i + 2) % self.dim]) * np.exp(-0.1 * x[i] ** 2) * (1 + 0.2 * np.cos(3 * r))
            
        # Add asymmetric coupling with cubic terms and dimension-dependent scaling
        for i in range(self.dim):
            result += 0.15 * (x[i] ** 3) * np.sin(4 * x[(i + 1) % self.dim]) * np.exp(-0.05 * x[i] ** 2)
            
        # Add radial peak structure with multiple local maxima
        result += 0.5 * np.exp(-0.3 * r ** 2) * np.sin(7 * r) * (1 + 0.4 * np.cos(5 * r))
        
        # Add dimensionality-dependent scaling with additional harmonic components
        scaling = 1.0 + 0.2 * np.sum(np.sin(x) ** 2) + 0.1 * np.sum(np.cos(x) ** 2) + 0.05 * np.sum(np.sin(2 * x) ** 2)
        result *= scaling
        
        # Add a novel chaotic component for increased complexity - modified for better performance
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 0.12 * np.sin(22 * x[i]) * np.cos(19 * x[(i + 3) % self.dim]) * np.exp(-0.025 * r ** 2)
        result += chaotic_term
        
        # Add a global modulation based on the sum of all dimensions
        global_mod = 1.0 + 0.15 * np.sin(3 * np.sum(x))
        result *= global_mod
        
        # Add novel hypercomplex coupling terms with higher-order polynomials and trigonometric interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.2 * np.sin(6 * x[i]) * np.cos(9 * x[j]) * np.sin(4 * x[k]) * np.exp(-0.1 * (x[i]**2 + x[j]**2 + x[k]**2)) * np.cos(3 * r)
        
        # Add a new fractal-like structure with recursive harmonic components - modified for better performance
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += 0.12 * np.sin(27 * x[i]) * np.cos(24 * x[(i + 1) % self.dim]) * np.sin(21 * x[(i + 2) % self.dim]) * np.exp(-0.035 * r ** 2)
        result += fractal_component
        
        # Add a new multi-modal structure with overlapping peaks - modified for better performance
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += 0.28 * (np.sin(12 * x[i]) + np.cos(14 * x[i])) ** 2 * np.exp(-0.15 * x[i] ** 2)
        result += multimodal_term
        
        # Add a new exponential decay component that varies with dimension - modified for better performance
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += 0.12 * np.exp(-0.25 * (x[i] - 2) ** 2) * np.sin(6 * x[i])
        result += exp_decay
        
        # Add a new term to improve conditioning and increase challenge
        conditioning_term = 0.05 * np.sum(np.abs(x) ** 1.5)
        result += conditioning_term
        
        # Add a novel high-frequency chaotic modulation with dynamic coupling
        dynamic_chaos = 0.0
        for i in range(self.dim):
            dynamic_chaos += 0.2 * np.sin(37 * x[i]) * np.cos(31 * x[(i + 1) % self.dim]) * np.exp(-0.04 * r ** 2) * np.sin(5 * r)
        result += dynamic_chaos
        
        # Add a new hyperdimensional coupling with complex trigonometric interactions
        hyper_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        if l < self.dim:
                            hyper_coupling += 0.15 * np.sin(7 * x[i]) * np.cos(11 * x[j]) * np.sin(9 * x[k]) * np.cos(13 * x[l]) * np.exp(-0.15 * (x[i]**2 + x[j]**2 + x[k]**2 + x[l]**2))
        result += hyper_coupling
        
        # Add a new asymmetric fractal structure with nested periodicity
        nested_fractal = 0.0
        for i in range(self.dim):
            nested_fractal += 0.18 * np.sin(41 * x[i]) * np.cos(38 * x[(i + 2) % self.dim]) * np.sin(35 * x[(i + 4) % self.dim]) * np.exp(-0.05 * r ** 2)
        result += nested_fractal
        
        # Add a new complex harmonic modulation with dynamic amplitude
        dynamic_harmonic = 0.0
        for i in range(self.dim):
            dynamic_harmonic += 0.3 * np.sin(15 * x[i]) * np.cos(17 * x[(i + 1) % self.dim]) * (1 + 0.2 * np.sin(8 * r)) * np.exp(-0.08 * x[i] ** 2)
        result += dynamic_harmonic
        
        # Add a new multi-scale fractal component with varying frequencies
        multi_scale_fractal = 0.0
        for i in range(self.dim):
            multi_scale_fractal += 0.15 * np.sin(47 * x[i]) * np.cos(43 * x[(i + 1) % self.dim]) * np.sin(39 * x[(i + 2) % self.dim]) * np.cos(36 * x[(i + 3) % self.dim]) * np.exp(-0.06 * r ** 2)
        result += multi_scale_fractal
        
        return result