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
        
        # Add a new component: ultra-high frequency chaotic modulation with memory effects
        memory = 0
        for i in range(self.dim):
            memory += (np.sin(10.0 * x[i]) * np.cos(15.0 * x[i]) * 
                      np.exp(-((x[i] - 1.0)**2 / 0.5)) * 
                      np.sin(np.pi * np.sin(np.pi * x[i])) + 
                      np.sin(8.0 * x[i]) * np.cos(12.0 * x[i]) * 
                      np.exp(-((x[i] + 1.0)**2 / 0.7)) * 
                      np.cos(np.pi * np.cos(np.pi * x[i])))
        
        # Add a new component: hybrid fractal-gaussian mixture with dimensional coupling
        fractal_gauss = 0
        for i in range(self.dim):
            fractal_gauss += (np.exp(-x[i]**2) * np.sin(5.0 * x[i]) * 
                             np.cos(3.0 * x[i]) * 
                             np.exp(-((x[i] - 0.5)**2 / 1.5)) + 
                             np.exp(-(x[i]**2)/2) * np.sin(7.0 * x[i]) * 
                             np.cos(4.0 * x[i]) * 
                             np.exp(-((x[i] + 0.8)**2 / 2.0)))
        
        # Add a new component: dynamic resonance landscape with time-like dimension coupling
        resonance = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                resonance += (np.sin(2.5 * x[i]) * np.cos(3.5 * x[j]) * 
                             np.exp(-((x[i] - x[j])**2 / 3.0)) + 
                             np.cos(1.8 * x[i]) * np.sin(2.2 * x[j]) * 
                             np.exp(-((x[i] + x[j])**2 / 4.0)))
        
        # Add a new component: modified chaotic landscape with enhanced nonlinearity
        nonlinear = 0
        for i in range(self.dim):
            nonlinear += (np.sin(5.0 * x[i]) * np.cos(8.0 * x[i]) * 
                         np.exp(-((x[i] - 1.2)**2 / 0.8)) * 
                         np.sin(np.pi * np.sin(2.0 * x[i])) + 
                         np.sin(3.5 * x[i]) * np.cos(6.0 * x[i]) * 
                         np.exp(-((x[i] + 1.3)**2 / 1.2)) * 
                         np.cos(np.pi * np.cos(1.5 * x[i])))
        
        # Add a new component: adaptive multimodal with dynamic scaling
        adaptive_multimodal = 0
        for i in range(self.dim):
            adaptive_multimodal += (np.sin(4.0 * x[i]) * np.cos(2.5 * x[i]) * 
                                  np.exp(-((x[i] - 2.0)**2 / 1.0)) * 
                                  (1 + 0.4 * np.sin(0.5 * i)) + 
                                  np.sin(1.5 * x[i]) * np.cos(3.0 * x[i]) * 
                                  np.exp(-((x[i] + 2.5)**2 / 1.5)) * 
                                  (1 + 0.3 * np.cos(0.7 * i)))
        
        # Add a new component: hybrid chaotic-polynomial with memory
        hybrid = 0
        for i in range(self.dim):
            hybrid += (np.sin(x[i]**2) * np.cos(x[i]) * 
                      np.exp(-((x[i] - 1.0)**2 / 0.5)) + 
                      np.cos(x[i]**3) * np.sin(x[i]) * 
                      np.exp(-((x[i] + 1.0)**2 / 0.8)))
        
        # Add a new component: enhanced chaotic landscape with multi-scale fractal characteristics
        multiscale = 0
        for i in range(self.dim):
            multiscale += (np.sin(6.0 * x[i]) * np.cos(4.0 * x[i]) * 
                          np.exp(-((x[i] - 1.0)**2 / 0.3)) * 
                          np.sin(np.pi * np.sin(3.0 * x[i])) + 
                          np.sin(2.0 * x[i]) * np.cos(5.0 * x[i]) * 
                          np.exp(-((x[i] + 1.5)**2 / 0.6)) * 
                          np.cos(np.pi * np.cos(2.0 * x[i])))
        
        # Add a new component: complex resonance with higher-order harmonics
        harmonic_resonance = 0
        for i in range(self.dim):
            harmonic_resonance += (np.sin(3.0 * x[i]) * np.cos(7.0 * x[i]) * 
                                 np.exp(-((x[i] - 0.5)**2 / 0.4)) + 
                                 np.sin(5.0 * x[i]) * np.cos(9.0 * x[i]) * 
                                 np.exp(-((x[i] + 0.8)**2 / 0.7)))
        
        # Add a new component: enhanced polynomial with multi-modal characteristics
        enhanced_poly = 0
        for i in range(self.dim):
            enhanced_poly += (x[i]**9 - 25*x[i]**7 + 200*x[i]**5 - 800*x[i]**3 + 600*x[i]) * 
                            np.exp(-((x[i] - 1.0)**2 / 1.0)) + 
                            (x[i]**6 - 15*x[i]**4 + 80*x[i]**2 - 60) * 
                            np.exp(-((x[i] + 1.0)**2 / 1.5))
        
        # Combine all components with new weights and scaling factors
        return (sphere * 0.03 + 
                multimodal * 0.35 + 
                chaotic * 0.25 + 
                poly * 0.85 + 
                interaction * 0.10 + 
                nested * 0.03 +
                memory * 0.12 +
                fractal_gauss * 0.06 +
                resonance * 0.04 +
                nonlinear * 0.08 +
                adaptive_multimodal * 0.07 +
                hybrid * 0.05 +
                multiscale * 0.15 +
                harmonic_resonance * 0.09 +
                enhanced_poly * 0.20)