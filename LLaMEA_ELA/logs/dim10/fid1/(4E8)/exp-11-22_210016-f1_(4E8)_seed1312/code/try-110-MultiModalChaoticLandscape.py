import numpy as np

class MultiModalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with polynomial chaos and symmetry breaking
        r = np.sqrt(np.sum(x**2))
        radial_term = (1.0 + 0.5 * np.sin(r * 2.0) + 0.3 * np.cos(r * 3.0)) * np.exp(-r**2 / 10.0)
        
        # Polynomial chaos component with high-order terms
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**2 + x[i]**4 + 0.1 * x[i]**6) * np.cos(x[i])
        
        # Trigonometric interference with multi-frequency components
        trig_interference = 0.0
        for i in range(self.dim):
            trig_interference += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]) + \
                               np.tanh(x[i]) * np.sin(2.0 * x[i]**2) + \
                               np.cos(4.0 * x[i]) * np.exp(-x[i]**2)
        
        # Cross-dimensional coupling with polynomial weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x[i] * x[j] * np.sin(x[i] + x[j])) / (1.0 + 0.1 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic modulation with radial symmetry breaking
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(x[i] * r) * np.cos(x[i]) * np.exp(-x[i]**2 / 5.0)
        
        # Multi-modal component with multiple local minima
        modal_component = 0.0
        for i in range(self.dim):
            modal_component += (np.sin(10.0 * x[i]) + 0.5 * np.cos(15.0 * x[i])) * \
                             (1.0 + 0.2 * np.sin(5.0 * x[i])**2)
        
        # Combine all terms with appropriate weights
        result = radial_term + 0.8 * poly_chaos + 0.6 * trig_interference + \
                 0.4 * cross_coupling + 0.3 * chaotic_mod + 0.5 * modal_component
        
        return result