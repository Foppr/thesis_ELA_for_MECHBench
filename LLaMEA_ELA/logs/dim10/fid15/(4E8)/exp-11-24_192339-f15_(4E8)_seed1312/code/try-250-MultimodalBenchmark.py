import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Octonion-inspired coupling terms with non-associative phase interactions
        oct_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-associative octonion-like interaction
                real_part = np.cos(x[i]) * np.sin(x[j]) - np.sin(x[i]) * np.cos(x[j])
                imag_part = np.sin(x[i]) * np.sin(x[j]) + np.cos(x[i]) * np.cos(x[j])
                oct_coupling += (real_part**2 + imag_part**2) * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Hyper-chaotic sine-cosine interactions with fractional frequency modulation
        hyper_chaotic = 0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.9 * np.sin(0.6 * x[i]**3) * np.cos(0.4 * x[i]) * np.tanh(0.2 * x[i])
            hyper_chaotic += np.sin(freq_mod * x[i]**1.5) * np.cos(freq_mod * x[i]**2.5) * np.tanh(x[i])
        
        # Multifractal radial basis functions with multi-scale log-log scaling
        multifractal_rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Multi-scale log-log scaled RBF with multifractal dimension
                scale = np.log(dist + 1.0) * np.log(dist + 2.0) * np.log(dist + 3.0)
                width = 0.6 + 0.4 * np.sin(0.5 * (x[i] + x[j]))
                multifractal_rbf += np.exp(-0.5 * (dist / width)**2) * np.sin(scale)
        
        # Hyperbolic tangent-based cross-dimensional interactions with variable coupling
        tanh_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.0 + 0.3 * np.sin(0.3 * (x[i] + x[j]))
                tanh_cross += np.tanh(x[i] + x[j]) * np.exp(-0.25 * (x[i] - x[j])**2) * coupling_strength
        
        # Dynamic exponential decay with multi-scale and multi-frequency modulation
        dynamic_decay = 0
        for i in range(self.dim):
            scale1 = 0.4 + 0.6 * np.sin(0.25 * x[i]**2)
            scale2 = 0.7 + 0.3 * np.cos(0.5 * x[i])
            freq_mod = 1.0 + 0.5 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[i]**2)
            dynamic_decay += np.exp(-scale1 * np.abs(x[i])) * np.exp(-scale2 * x[i]**2) * np.sin(freq_mod * x[i])
        
        # Spherical harmonic with variable degree and multi-dimensional coupling
        sph_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x[i]**2 + x[j]**2)
                degree = 1 + int(4 * np.sin(0.6 * dist) * np.cos(0.3 * dist))
                sph_coupling += (np.sin(degree * dist) * np.cos(degree * dist)) / (dist + 1e-8)
        
        # Asymmetric power-law with oscillating exponents and multi-scale modulation
        asym_power = 0
        for i in range(self.dim):
            exp_factor = 2.5 + 1.0 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i]**2)
            scale_mod = 0.8 + 0.2 * np.sin(0.4 * x[i])
            asym_power += (np.abs(x[i])**exp_factor) * np.exp(-0.15 * x[i]**2) * scale_mod
        
        # Global conditioning with hyper-chaotic modulation
        cond_factor = 2.0 + 0.5 * np.sin(self.dim * 0.4) * np.cos(self.dim * 0.2) * np.tanh(0.1 * self.dim)
        
        # Combine all components with optimized weights
        return cond_factor * (0.16 * oct_coupling + 0.20 * hyper_chaotic + 
                             0.17 * multifractal_rbf + 0.13 * tanh_cross + 
                             0.14 * dynamic_decay + 0.11 * sph_coupling + 
                             0.19 * asym_power)