import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic quaternion-based oscillation with fractional Brownian motion correlations
        chaotic_quat = 0
        for i in range(self.dim):
            # Quaternion-inspired multi-dimensional coupling
            q_real = np.cos(0.2 * x[i])
            q_imag1 = np.sin(0.2 * x[i]) * np.cos(0.3 * x[i])
            q_imag2 = np.sin(0.2 * x[i]) * np.sin(0.3 * x[i])
            q_imag3 = np.cos(0.2 * x[i]) * np.sin(0.3 * x[i])
            
            # Fractional Brownian motion scaling
            hurst = 0.7 + 0.2 * np.sin(0.1 * i)
            fbm_scale = np.power(np.abs(x[i]), 2 * hurst)
            
            chaotic_quat += (q_real * q_imag1 * q_imag2 * q_imag3) * fbm_scale
        
        # Fractional polynomial coupling with dynamic conditioning
        frac_poly = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractional power coupling with dynamic exponent
                alpha = 1.5 + 0.5 * np.sin(0.2 * (x[i] + x[j]))
                frac_poly += np.power(np.abs(x[i] - x[j]), alpha) * np.cos(0.5 * (x[i] + x[j]))
        
        # Topological twist interactions with anti-symmetric cross-dimensional coupling
        twist = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Twist-based interaction with phase modulation
                phase = np.sin(0.4 * x[i]) * np.cos(0.4 * x[j])
                twist += (x[i] * x[j] * phase) * np.exp(-0.3 * (x[i] - x[j])**2)
        
        # Hyperbolic tangent-based non-separable coupling with dynamic frequency
        tan_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 2.0 + np.sin(0.3 * x[i]) * np.cos(0.3 * x[j])
                tan_coupling += np.tanh(freq * (x[i] + x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric skewing with recursive fractal-like structure
        skew = 0
        for i in range(self.dim):
            # Recursive skew factor with dynamic scaling
            scale = 1.0 + 0.4 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.7 * x[i]**2)
            skew += np.tanh(x[i] * scale) * np.exp(-0.1 * x[i]**2)
        
        # Dynamic conditioning with polynomial scaling and anti-symmetric terms
        cond = 0
        for i in range(self.dim):
            poly_term = x[i]**5 + 0.6 * x[i]**4 + 0.3 * x[i]**3
            asym_term = np.sin(0.2 * x[i]) * np.cos(0.2 * x[i])
            cond += poly_term * asym_term
        
        # Novel noise component with topological twist
        noise = 0
        for i in range(self.dim):
            # Topologically twisted noise
            twist_noise = np.sin(3 * x[i]) * np.cos(5 * x[i]) - np.cos(3 * x[i]) * np.sin(5 * x[i])
            noise += 0.15 * twist_noise * np.tanh(1.5 * x[i])
        
        # Global scaling factor with dynamic dimensionality effect
        global_scale = 1.0 + 0.25 * np.sin(self.dim * 0.15) + 0.2 * np.cos(self.dim * 0.1)
        
        # Combine all components with optimized weights for maximum difficulty
        return global_scale * (0.25 * chaotic_quat + 0.2 * frac_poly + 0.15 * twist + 
                              0.15 * tan_coupling + 0.1 * skew + 0.1 * cond + 0.05 * noise)