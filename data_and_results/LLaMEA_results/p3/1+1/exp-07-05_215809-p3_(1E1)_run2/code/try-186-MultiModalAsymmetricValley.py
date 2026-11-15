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
        
        # Add new chaotic and fractal components for increased complexity
        for i in range(self.dim):
            f += 0.18 * np.sin(33 * x[i]) * np.cos(39 * x[i]) * np.sin(45 * x[i]) * np.cos(51 * x[i])
            
        # Introduce cross-dimensional coupling with non-linear interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                f += 0.25 * np.sin(x[i]**2 + x[j]**2) * np.cos(x[i] * x[j]) * np.sin(x[i] * x[j] + 0.5)
                
        # Add irregular high-frequency oscillations
        for i in range(self.dim):
            f += 0.12 * np.sin(60 * x[i]) * np.cos(65 * x[i]) * np.sin(70 * x[i]) * np.cos(75 * x[i])
            
        # Introduce multi-scale fractal-like structure with recursive harmonic terms
        for i in range(self.dim):
            f += 0.08 * np.sin(80 * x_norm[i]) * np.cos(85 * x_norm[i]) * np.sin(90 * x_norm[i]) * np.cos(95 * x_norm[i]) * np.sin(100 * x_norm[i])
            
        # Enhanced gradient modulation with multi-scale characteristics
        gradient_mod2 = 0.0
        for i in range(self.dim):
            gradient_mod2 += 0.03 * np.sin(13 * x[i]) * np.cos(17 * x[i]) * np.sin(21 * x[i]) * np.cos(25 * x[i])
        f += gradient_mod2
        
        # Add a new global perturbation term for additional challenge
        global_pert = 0.0
        for i in range(self.dim):
            global_pert += 0.05 * np.sin(100 * x[i]) * np.cos(110 * x[i])
        f += global_pert
        
        return f