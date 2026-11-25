import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with altered dynamic frequency modulation
        chaotic_component = 0
        for i in range(self.dim):
            freq = 1.5 + 2.0 * np.sin(0.4 * x[i] + 0.6 * np.cos(0.5 * x[i]))
            chaotic_component += np.sin(freq * x[i]) * np.cos(0.3 * x[i]**2) * np.exp(-0.15 * np.abs(x[i]))
        
        # Dynamic radial basis function with modified quaternion-inspired coupling
        rbf_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 0.8 + 0.7 * np.sin(0.6 * x[i] + 0.4 * x[j])
                # Quaternion-inspired asymmetric coupling with modified weights
                quat_coupling = (x[i]**2 * x[j] + 0.5 * x[j]**2 * x[i]) * np.exp(-0.4 * (dist / width)**2)
                rbf_component += quat_coupling
        
        # Hyperbolic tangent-based cross-dimensional interaction with altered coefficients
        tan_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tan_mod = np.tanh(1.5 * x[i] * x[j] + 0.3 * np.sin(x[i] + x[j]))
                tan_term = (x[i]**2 + 0.8 * x[j]) * tan_mod * np.exp(-0.15 * (x[i] - x[j])**2)
                tan_component += tan_term
        
        # Fractal-like asymmetric polynomial with adjusted scaling
        fractal_poly = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic scale factor with modified chaotic modulation
                scale = 1.2 + 0.2 * np.sin(1.8 * x[i] + 0.5 * x[j]) * np.cos(1.2 * x[i])
                fractal_poly += (x[i]**3 - 0.8 * x[j]**2) * scale
        
        # Exponential decay with modified chaotic modulation
        exp_component = 0
        for i in range(self.dim):
            exp_component += np.exp(-0.25 * x[i]**2) * np.sin(0.2 * self.dim * x[i] + 0.3 * np.cos(x[i]))
        
        # Global scaling factor with altered chaotic influence
        scale_factor = 1.0 + 0.15 * np.sin(0.5 * self.dim + 0.7 * np.cos(0.4 * x[0] if self.dim > 0 else 0))
        
        # Combine all components with updated weights for enhanced discrimination
        return scale_factor * (0.25 * chaotic_component + 0.3 * rbf_component + 
                              0.18 * tan_component + 0.17 * fractal_poly + 0.1 * exp_component)