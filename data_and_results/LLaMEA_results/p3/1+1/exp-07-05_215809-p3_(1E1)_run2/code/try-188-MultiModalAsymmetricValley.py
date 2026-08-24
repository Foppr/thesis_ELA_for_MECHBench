import numpy as np

class MultiModalAsymmetricValley:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic component with varying frequencies and amplitudes
        f = 0.0
        for i in range(self.dim):
            f += 0.5 * np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) + 0.3 * np.sin(5 * x_norm[i]) * np.cos(7 * x_norm[i])
            
        # Asymmetric saddle points with directional bias
        for i in range(self.dim):
            # Asymmetric quadratic with dynamic bias
            bias = 0.4 * np.sin(i * 0.8) + 0.2 * np.cos(i * 1.2)
            f += (0.5 * x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.1 * np.sinh(x[i]**2)
            
        # Multi-scale coupling with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Dynamic weight based on dimension indices
                weight = 0.3 * np.sin(i * 0.5) * np.cos(j * 0.7) + 0.2 * np.sin(i + j * 0.3)
                f += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Fractal-like structure with recursive harmonic terms
        for i in range(self.dim):
            f += 0.2 * np.sin(11 * x_norm[i]) * np.cos(13 * x_norm[i]) * np.sin(17 * x_norm[i])
            
        # Chaotic perturbations with irregular frequency components
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i]) * np.sin(29 * x_norm[i]) * np.cos(31 * x_norm[i])
        f += 0.15 * chaos
        
        # Multi-modal structure with irregular peaks and valleys
        for i in range(self.dim):
            f += 0.25 * np.sin(8 * x[i]) * np.cos(12 * x[i]) * np.sin(16 * x[i])
            
        # Dynamic gradient modulation based on proximity to critical points
        proximity = 0.0
        for i in range(self.dim):
            proximity += np.abs(x[i] - np.sin(i * 0.6)) + 0.1 * np.abs(x[i] - np.cos(i * 0.4))
        scale_factor = 1.0 + 0.5 * np.exp(-proximity / 2.0)
        f *= scale_factor
        
        # Additional harmonic coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.2 * np.exp(-0.1 * (i + j)) * np.sin(i * 0.3) * np.cos(j * 0.4)
                f += weight * np.sin(2 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 2 * x[j])
                
        # Enhanced saddle point structure with irregular perturbations
        for i in range(self.dim):
            f += 0.3 * np.sin(3 * x[i]) * np.cos(4 * x[i]) * np.sin(5 * x[i]) * np.cos(6 * x[i])
            
        # Additional fractal-like complexity with nested terms
        for i in range(self.dim):
            f += 0.1 * np.sin(37 * x_norm[i]) * np.cos(41 * x_norm[i]) * np.sin(43 * x_norm[i]) * np.cos(47 * x_norm[i])
            
        # Multi-scale periodicity with non-uniform frequencies
        periodicity = 0.0
        for i in range(self.dim):
            periodicity += 0.15 * np.sin(25 * x[i]) * np.cos(30 * x[i]) * np.sin(35 * x[i])
        f += periodicity
        
        # Final scaling to ensure proper fitness landscape characteristics
        f *= 1.0 + 0.1 * np.sum(np.abs(x))
        
        # Add higher-order polynomial terms for additional curvature
        f += 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Introduce improved gradient characteristics
        gradient_mod = 0.0
        for i in range(self.dim):
            gradient_mod += 0.05 * np.sin(7 * x[i]) * np.cos(9 * x[i]) * np.sin(11 * x[i])
        f += gradient_mod
        
        # Add noise-like perturbations to improve robustness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(50 * x[i]) * np.cos(55 * x[i])
        f += noise
        
        # Adjust for better conditioning
        f = f * (1.0 + 0.05 * np.std(x))
        
        # Introduce new chaotic behavior with higher frequency components
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += 0.1 * np.sin(61 * x[i]) * np.cos(67 * x[i]) * np.sin(71 * x[i]) * np.cos(73 * x[i])
        f += chaotic_component
        
        # Add new multi-modal structure with complex interaction terms
        multimodal_component = 0.0
        for i in range(self.dim):
            multimodal_component += 0.3 * np.sin(9 * x[i]) * np.cos(14 * x[i]) * np.sin(18 * x[i]) * np.cos(22 * x[i])
        f += multimodal_component
        
        # Introduce new fractal-like complexity with nested harmonic terms
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += 0.15 * np.sin(83 * x_norm[i]) * np.cos(89 * x_norm[i]) * np.sin(97 * x_norm[i]) * np.cos(101 * x_norm[i])
        f += fractal_component
        
        # Add new dynamic coupling with time-dependent weights
        dynamic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                time_weight = 0.25 * np.sin(i * 0.4 + j * 0.3) * np.cos(i * 0.2 + j * 0.5)
                dynamic_coupling += time_weight * np.sin(x[i] + 2*x[j]) * np.cos(2*x[i] - x[j])
        f += dynamic_coupling
        
        # Introduce new asymmetric behavior with exponential scaling
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += 0.2 * np.exp(-0.5 * x[i]**2) * np.sin(13 * x[i]) * np.cos(15 * x[i])
        f += asymmetry
        
        # Add new complex periodic structure with varying amplitudes
        complex_periodic = 0.0
        for i in range(self.dim):
            complex_periodic += 0.18 * np.sin(33 * x[i]) * np.cos(39 * x[i]) * np.sin(45 * x[i]) * np.cos(51 * x[i])
        f += complex_periodic
        
        return f