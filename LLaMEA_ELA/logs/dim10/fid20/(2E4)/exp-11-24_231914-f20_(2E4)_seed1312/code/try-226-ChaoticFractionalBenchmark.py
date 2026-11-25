import numpy as np

class ChaoticFractionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters
        self.tent_r = np.random.uniform(1.5, 3.9, size=dim)
        self.tent_offset = np.random.uniform(-0.5, 0.5, size=dim)
        # Fractional Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, size=dim)
        self.fb_scale = np.random.uniform(0.5, 2.0, size=dim)
        # Quantum-inspired amplitude modulation
        self.quantum_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.quantum_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Multi-scale interaction weights
        self.weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Basin attraction parameters
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=(5, dim))
        self.basin_strengths = np.random.uniform(0.5, 2.5, size=5)
        # Fractional derivatives for complex dynamics
        self.fractional_order = np.random.uniform(0.3, 0.8, size=dim)
        # Coupling strength and delay parameters
        self.coupling_strength = np.random.uniform(0.1, 1.5, size=dim)
        self.delay = np.random.randint(1, 4, size=dim)
        # Nonlinear damping coefficients
        self.damping = np.random.uniform(0.01, 0.3, size=dim)
        # Multi-modal peak parameters
        self.peak_heights = np.random.uniform(1.0, 5.0, size=dim)
        self.peak_widths = np.random.uniform(0.2, 1.5, size=dim)
        
    def tent_map(self, x, r):
        return r * x * (1 - x)
    
    def fractional_brownian(self, x, hurst, scale):
        # Simplified fractional Brownian motion approximation
        return scale * np.sin(hurst * x) + 0.3 * np.cos(2 * hurst * x)
    
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component
        tent_component = 0.0
        for i in range(self.dim):
            # Apply tent map dynamics with offset
            tent_val = self.tent_map(np.abs(x[i]), self.tent_r[i])
            tent_component += tent_val * np.exp(-self.tent_offset[i] * x[i]**2)
        
        # Fractional Brownian motion component
        fb_component = 0.0
        for i in range(self.dim):
            fb_component += self.fractional_brownian(x[i], self.hurst[i], self.fb_scale[i])
            
        # Quantum-inspired amplitude modulation
        quantum_component = 0.0
        for i in range(self.dim):
            amp_mod = self.quantum_amp[i] * (1 + 0.5 * np.sin(self.quantum_phase[i] + x[i]))
            quantum_component += amp_mod * np.cos(x[i]**2) * np.exp(-x[i]**2/10)
            
        # Multi-scale coupling with interaction weights
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.weights[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Basin attraction component with multiple local minima
        basin_component = 0.0
        for k in range(5):
            dist_sum = 0.0
            for i in range(self.dim):
                dist = np.abs(x[i] - self.basin_centers[k, i])
                dist_sum += dist**2
            basin_component += self.basin_strengths[k] * np.exp(-dist_sum/10)
            
        # Fractional derivative dynamics
        frac_component = 0.0
        for i in range(self.dim):
            frac_val = np.sin(self.fractional_order[i] * x[i]) * np.cos(x[i])
            frac_component += frac_val * self.fb_scale[i]
            
        # Coupling with delay and damping
        delay_component = 0.0
        for i in range(self.dim):
            delayed_x = x[(i - self.delay[i]) % self.dim]
            delay_component += (self.coupling_strength[i] * 
                              np.sin(x[i] + delayed_x) * 
                              np.exp(-self.damping[i] * x[i]**2))
        
        # Multi-modal peak component
        peak_component = 0.0
        for i in range(self.dim):
            peak_val = 0.0
            for j in range(3):  # Multiple peaks per dimension
                peak_center = np.random.uniform(-4, 4)
                peak_width = self.peak_widths[i]
                peak_height = self.peak_heights[i]
                peak_val += peak_height * np.exp(-((x[i] - peak_center)**2) / (2 * peak_width**2))
            peak_component += peak_val
            
        # Combined fitness function with balanced weights
        return (1.5 * tent_component + 
                1.3 * fb_component + 
                1.2 * quantum_component + 
                1.8 * coupling_component + 
                1.0 * basin_component + 
                0.8 * frac_component + 
                0.9 * delay_component + 
                0.7 * peak_component)