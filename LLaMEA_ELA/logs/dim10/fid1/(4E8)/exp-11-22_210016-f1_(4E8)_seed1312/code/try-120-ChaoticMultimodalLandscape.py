import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with polynomial chaos and symmetry breaking
        r = np.sqrt(np.sum(x**2))
        radial_term = (1.0 + 0.3 * np.sin(r * 2.5) + 0.4 * np.cos(r * 3.5)) * np.exp(-r**2 / 8.0)
        
        # Polynomial chaos component with high-order terms
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**2 + 0.8 * x[i]**4 + 0.15 * x[i]**6) * np.cos(x[i])
        
        # Trigonometric interference with multi-frequency components
        trig_interference = 0.0
        for i in range(self.dim):
            trig_interference += np.sin(4.0 * x[i]) * np.cos(2.5 * x[i]) + \
                               np.tanh(x[i]) * np.sin(1.5 * x[i]**2) + \
                               np.cos(3.5 * x[i]) * np.exp(-x[i]**2 / 1.5)
        
        # Cross-dimensional coupling with polynomial weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))) / (1.0 + 0.05 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic modulation with radial symmetry breaking
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(1.2 * x[i] * r) * np.cos(0.8 * x[i]) * np.exp(-x[i]**2 / 4.0)
        
        # Multi-modal component with multiple local minima
        modal_component = 0.0
        for i in range(self.dim):
            modal_component += (np.sin(12.0 * x[i]) + 0.6 * np.cos(18.0 * x[i])) * \
                             (1.0 + 0.3 * np.sin(6.0 * x[i])**2)
        
        # Combine all terms with appropriate weights
        result = radial_term + 0.9 * poly_chaos + 0.7 * trig_interference + \
                 0.5 * cross_coupling + 0.4 * chaotic_mod + 0.6 * modal_component
        
        return result