import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic quaternion-inspired component with dynamic frequency modulation
        chaotic_quat = 0
        for i in range(self.dim):
            # Dynamic frequency modulation based on position
            freq_mod1 = 2.0 + 1.2 * np.sin(0.4 * x[i] + 0.3 * np.cos(x[i]))
            freq_mod2 = 1.5 + 0.9 * np.cos(0.5 * x[i] + 0.2 * np.sin(x[i]))
            # Quaternion-like interaction terms
            quat_real = np.cos(0.3 * x[i]) * np.cos(0.4 * x[i]**2)
            quat_imag = np.sin(0.3 * x[i]) * np.sin(0.4 * x[i]**2)
            chaotic_quat += (quat_real + quat_imag) * np.sin(freq_mod1 * x[i] + freq_mod2 * np.cos(x[i]))
        
        # Fractal-based radial basis function with anti-symmetric coupling
        fractal_rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                # Fractal scaling factor
                scale = 1.0 + 0.3 * np.sin(0.6 * (x[i] + x[j]))
                # Anti-symmetric coupling with hyperbolic terms
                asym_coupling = np.tanh(x[i]) * np.cosh(x[j]) - np.tanh(x[j]) * np.cosh(x[i])
                fractal_rbf += asym_coupling * np.exp(-0.5 * (dist / scale)**2) * np.sin(dist)
        
        # Novel asymmetric polynomial coupling with dynamic weights
        asym_poly = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on dimensionality and position
                weight = 1.0 + 0.2 * np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * self.dim)
                # Asymmetric polynomial interaction
                asym_term = (x[i]**3 - x[j]**3) * np.tanh(x[i] + x[j]) * weight
                asym_poly += asym_term
        
        # Hyperbolic tangent-based cross-dimensional interactions with recursive structure
        tan_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive hyperbolic coupling
                tan_coupling = np.tanh(x[i] * x[j]) + 0.5 * np.tanh((x[i] + x[j])**2) + 0.3 * np.tanh((x[i] - x[j])**3)
                tan_cross += tan_coupling * (1.0 + 0.1 * np.sin(0.4 * x[i]) * np.cos(0.4 * x[j]))
        
        # Anti-symmetric skewing with fractal-like recursive structure
        skew_fractal = 0
        for i in range(self.dim):
            # Recursive asymmetric skewing with fractal scaling
            fractal_scale = 1.0 + 0.25 * np.sin(0.7 * x[i]) * np.cos(0.8 * x[i]**2)
            skew_fractal += (np.tanh(x[i]) - np.tanh(-x[i])) * fractal_scale
        
        # Dynamic conditioning with multi-scale polynomial terms
        cond_multiscale = 0
        for i in range(self.dim):
            # Multi-scale polynomial conditioning
            cond_multiscale += (x[i]**5 + 0.6 * x[i]**4 + 0.3 * x[i]**3) * np.sin(0.2 * x[i]) * (1.0 + 0.15 * np.cos(0.5 * self.dim))
        
        # Novel noise component with anti-symmetric quaternion interactions
        noise_quat = 0
        for i in range(self.dim):
            # Anti-symmetric quaternion-inspired noise
            quat_noise = np.sin(6 * x[i]) * np.cos(8 * x[i]) - np.cos(6 * x[i]) * np.sin(8 * x[i])
            noise_quat += 0.12 * quat_noise * np.tanh(3 * x[i])
        
        # Additional asymmetric coupling with novel fractal structure
        fractal_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Novel anti-symmetric fractal coupling
                fractal_term = (np.tanh(x[i]) - np.tanh(x[j])) * np.exp(-0.3 * (x[i] - x[j])**2) + 0.2 * np.sin(0.5 * (x[i] + x[j]))
                fractal_coupling += fractal_term
        
        # Global scaling factor with dynamic dimensionality influence
        global_scale = 1.0 + 0.4 * np.sin(self.dim * 0.15) * np.cos(self.dim * 0.08)
        
        # Combine all components with optimized weights for maximum complexity and discrimination
        return global_scale * (0.25 * chaotic_quat + 0.2 * fractal_rbf + 0.18 * asym_poly + 
                              0.15 * tan_cross + 0.1 * skew_fractal + 0.07 * cond_multiscale + 
                              0.05 * fractal_coupling) + noise_quat