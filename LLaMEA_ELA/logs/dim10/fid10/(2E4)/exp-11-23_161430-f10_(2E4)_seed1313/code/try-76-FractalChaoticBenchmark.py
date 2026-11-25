import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic tent map parameters with time-varying dynamics
        self.amp = 2.0 + 1.5 * np.sin(np.arange(dim) * 0.4 + np.pi/5)
        self.beta = 0.8 + 0.7 * np.cos(np.arange(dim) * 0.5 + np.pi/4)
        # Fractal Brownian motion with time-varying Hurst and multi-scale modulation
        self.hurst = 0.15 + 0.75 * np.random.rand(dim)
        self.fractal_scale = 3.0 + 2.0 * np.sin(np.arange(dim) * 0.3 + np.pi/7)
        # Quaternion-inspired radial basis function parameters
        self.rbf_centers = np.linspace(-4.8, 4.8, min(10, dim // 2 + 3))
        self.rbf_scales = np.linspace(0.6, 3.5, min(6, dim // 3 + 2))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced modulation and time-varying dynamics
        tent_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Tent map with adaptive amplitude and phase
            if xi < 0.5:
                tent_val = self.amp[i] * xi
            else:
                tent_val = self.amp[i] * (1 - xi)
            # Multi-frequency chaotic modulation with temporal coupling
            tent_term += tent_val * np.sin(self.beta[i] * xi + i * 0.2) * \
                        np.cos(0.3 * xi * (i + 1)) * np.exp(-0.08 * i**1.9)
        
        # Fractal Brownian motion with time-varying Hurst and enhanced noise
        fbm_term = 0.0
        for i in range(self.dim):
            # Generate fractal noise with improved correlation structure
            noise_val = np.random.normal(0, 1) * self.fractal_scale[i]
            # Enhanced positional dependence with periodic and hyperbolic components
            fbm_term += noise_val * np.cos(3.0 * np.pi * x[i] * (i + 1) + i * 0.4) * \
                       np.tanh(0.15 * x[i]**2) * np.exp(-0.05 * (x[i]**2 + i**2.2))
        
        # Enhanced multi-scale radial basis function with quaternion-like interactions
        rbf_term = 0.0
        for level, scale in enumerate(self.rbf_scales):
            for i, center in enumerate(self.rbf_centers):
                if i >= self.dim:
                    break
                sigma = scale * (1.0 + 0.5 * np.sin(i * 0.9 + level * 0.7))
                # Quaternion-inspired RBF with multi-directional components
                rbf_term += np.exp(-0.5 * ((x[i] - center) / sigma)**2) * \
                           np.sin(4.0 * np.pi * (x[i] - center) / sigma + level * 0.6) * \
                           np.cos(2.0 * (x[i] - center) / sigma) * \
                           np.tanh(0.6 * (x[i] - center)**2)
        
        # Hyper-saddle point structure with enhanced curvature and phase shifts
        saddle_term = 0.0
        for i in range(self.dim):
            base = x[i]
            # Hyper-saddle with variable curvature and multi-scale phase modulation
            saddle_term += (base**9 - 9*base**7 + 28*base**5 - 35*base**3 + 15*base) * \
                          np.cos(0.5 * base + i * 0.3) * np.sin(0.4 * base**2 + i * 0.15) * \
                          np.exp(-0.12 * i)
        
        # Non-linear cross-dimensional coupling with enhanced interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 3) % self.dim
            k = (i + 5) % self.dim
            l = (i + 2) % self.dim
            # Enhanced coupling with variable weights and multi-scale interaction terms
            weight = 2.0 + 0.6 * np.sin(i * 0.7 + x[j] * 0.35) * np.cos(x[k] * 0.45) * \
                    np.tanh(0.25 * x[l])
            cross_term += weight * np.sin(5.0 * x[i] + i * 0.15) * np.cos(4.0 * x[j] + j * 0.2) * \
                         np.tanh(1.0 * (x[k] - x[i])) * np.exp(-0.1 * (x[i]**2 + x[j]**2 + x[k]**2))
        
        # Combine all components with adjusted weights for better balance and challenge
        result = 0.4 * np.sum(x**2) + 0.3 * tent_term + 0.25 * fbm_term + \
                 0.18 * rbf_term + 0.07 * saddle_term + 0.05 * cross_term
        
        return result