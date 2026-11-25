import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with nested chaotic behavior and fractal scaling
        multimodal = 0
        for i in range(self.dim):
            # Nested chaotic mappings with varying scales
            term1 = np.sin(2.3 * x[i]) * np.cos(3.7 * x[i]) * np.exp(-((x[i] - np.pi)**2 / 3.0))
            term2 = np.sin(4.1 * x[i]) * np.cos(1.9 * x[i]) * np.exp(-((x[i] + np.pi)**2 / 8.0))
            term3 = np.sin(0.5 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-((x[i] - 3*np.pi)**2 / 10.0))
            term4 = np.sin(1.7 * x[i]) * np.cos(2.9 * x[i]) * np.exp(-((x[i] + 2.5)**2 / 6.0))
            multimodal += (term1 + term2 + term3 + term4) * (1 + 0.3 * np.sin(0.1 * x[i])**2)
            
        # Enhanced chaotic component with adaptive scaling and cross-dimension dependencies
        chaotic = 0
        for i in range(self.dim):
            # Adaptive chaotic mapping with dimension-dependent scaling
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * i)
            chaotic += (np.sin(x[i] * np.exp(-0.4 * x[i]**2)) * np.cos(x[i] * np.exp(-0.2 * x[i]**2)) * 
                       np.exp(-((x[i] - 1.5)**2 / 3.0)) * scale_factor + 
                       np.sin(0.9 * x[i] * np.cos(0.7 * x[i])) * np.cos(1.3 * x[i] * np.sin(0.6 * x[i])) * 
                       np.exp(-((x[i] + 2.0)**2 / 7.0)) * scale_factor)
            
        # Polynomial component with fractal-like behavior and higher-order interactions
        poly = 0
        for i in range(self.dim):
            # Fractal-inspired polynomial with adaptive coefficients
            coef = 1.0 + 0.2 * np.sin(0.5 * i)
            poly += (coef * (x[i]**7 - 15*x[i]**5 + 60*x[i]**3 - 40*x[i]) * 
                    np.exp(-((x[i] - 2.0)**2 / 2.0)) + 
                    0.5 * (x[i]**8 - 20*x[i]**6 + 150*x[i]**4 - 400*x[i]**2) * 
                    np.exp(-((x[i] + 1.5)**2 / 5.0)))
            
        # Complex interaction terms with adaptive weights and fractal-like dependencies
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like interaction with dimension-dependent scaling
                weight_factor = 1.0 + 0.3 * np.sin(0.2 * (i + j))
                interaction += (weight_factor * 
                               (np.sin(1.5*x[i]) * np.cos(0.7*x[j]) * np.exp(-((x[i] - x[j])**2 / 5.0)) +
                                np.cos(0.8*x[i]) * np.sin(1.3*x[j]) * np.exp(-((x[i] + x[j])**2 / 9.0))) +
                               (np.sin(2.1*x[i]) * np.cos(1.2*x[j]) * np.exp(-((x[i] - 0.5*x[j])**2 / 4.0)) +
                                np.cos(1.8*x[i]) * np.sin(0.9*x[j]) * np.exp(-((x[i] + 0.7*x[j])**2 / 6.0))))
        
        # Add a new component: nested chaotic landscape with self-similar properties
        nested = 0
        for i in range(self.dim):
            nested += (np.sin(3.2 * x[i]) * np.cos(2.1 * x[i]) * 
                      np.exp(-((x[i] - np.pi/2)**2 / 4.0)) * 
                      np.sin(np.pi * np.sin(x[i])) + 
                      np.sin(1.9 * x[i]) * np.cos(3.8 * x[i]) * 
                      np.exp(-((x[i] + np.pi/3)**2 / 6.0)) * 
                      np.cos(np.pi * np.cos(x[i])))
        
        # Add a slight modification to the interaction term weights and polynomial coefficients
        modified_interaction = interaction * 1.1
        modified_poly = poly * 0.9
        
        # Combine all components with new weights and scaling factors
        return (sphere * 0.05 + 
                multimodal * 0.40 + 
                chaotic * 0.30 + 
                modified_poly + 
                modified_interaction * 0.08 + 
                nested * 0.02)