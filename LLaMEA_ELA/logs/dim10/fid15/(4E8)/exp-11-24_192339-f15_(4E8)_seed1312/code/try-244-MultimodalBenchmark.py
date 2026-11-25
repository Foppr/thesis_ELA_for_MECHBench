import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-inspired coupling terms with complex phase interactions
        quat_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Complex quaternion-like interaction
                real_part = np.cos(x[i]) * np.sin(x[j])
                imag_part = np.sin(x[i]) * np.cos(x[j])
                quat_coupling += (real_part**2 + imag_part**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Chaotic sine-cosine interactions with dynamic frequency modulation
        chaotic_interaction = 0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.8 * np.sin(0.5 * x[i]**3) * np.cos(0.3 * x[i])
            chaotic_interaction += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**2) * np.tanh(x[i])
        
        # Fractal-based radial basis functions with log-log scaling
        fractal_rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Log-log scaled RBF with fractal dimension
                scale = np.log(dist + 1.0) * np.log(dist + 2.0)
                width = 0.5 + 0.5 * np.sin(0.4 * (x[i] + x[j]))
                fractal_rbf += np.exp(-0.5 * (dist / width)**2) * np.sin(scale)
        
        # Hyperbolic tangent-based cross-dimensional interactions
        tanh_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tanh_cross += np.tanh(x[i] + x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Dynamic exponential decay with multi-scale modulation
        dynamic_decay = 0
        for i in range(self.dim):
            scale1 = 0.3 + 0.7 * np.sin(0.2 * x[i]**2)
            scale2 = 0.8 + 0.2 * np.cos(0.4 * x[i])
            dynamic_decay += np.exp(-scale1 * np.abs(x[i])) * np.exp(-scale2 * x[i]**2) * np.sin(2 * x[i])
        
        # Spherical harmonic with variable degree coupling
        sph_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x[i]**2 + x[j]**2)
                degree = 1 + int(3 * np.sin(0.5 * dist))
                sph_coupling += (np.sin(degree * dist) * np.cos(degree * dist)) / (dist + 1e-8)
        
        # Asymmetric power-law with oscillating exponents
        asym_power = 0
        for i in range(self.dim):
            exp_factor = 2.0 + 1.5 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i]**2)
            asym_power += (np.abs(x[i])**exp_factor) * np.exp(-0.1 * x[i]**2)
        
        # Global conditioning with chaotic modulation
        cond_factor = 1.5 + 0.5 * np.sin(self.dim * 0.3) * np.cos(self.dim * 0.1)
        
        # Combine all components with optimized weights
        return cond_factor * (0.18 * quat_coupling + 0.22 * chaotic_interaction + 
                             0.15 * fractal_rbf + 0.12 * tanh_cross + 
                             0.13 * dynamic_decay + 0.10 * sph_coupling + 
                             0.08 * asym_power)