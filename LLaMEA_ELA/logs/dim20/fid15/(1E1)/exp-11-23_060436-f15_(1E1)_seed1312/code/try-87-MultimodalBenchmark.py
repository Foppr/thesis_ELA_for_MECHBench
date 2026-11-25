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
            # Modified chaotic mappings with different scales and frequencies
            term1 = np.sin(2.5 * x[i]) * np.cos(3.5 * x[i]) * np.exp(-((x[i] - np.pi)**2 / 2.5))
            term2 = np.sin(4.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-((x[i] + np.pi)**2 / 7.0))
            term3 = np.sin(0.6 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-((x[i] - 3*np.pi)**2 / 9.0))
            term4 = np.sin(1.8 * x[i]) * np.cos(2.8 * x[i]) * np.exp(-((x[i] + 2.5)**2 / 5.0))
            multimodal += (term1 + term2 + term3 + term4) * (1 + 0.25 * np.sin(0.15 * x[i])**2)
            
        # Enhanced chaotic component with adaptive scaling and cross-dimension dependencies
        chaotic = 0
        for i in range(self.dim):
            # Modified chaotic mapping with dimension-dependent scaling
            scale_factor = 1.0 + 0.4 * np.sin(0.35 * i)
            chaotic += (np.sin(x[i] * np.exp(-0.35 * x[i]**2)) * np.cos(x[i] * np.exp(-0.15 * x[i]**2)) * 
                       np.exp(-((x[i] - 1.4)**2 / 2.5)) * scale_factor + 
                       np.sin(0.85 * x[i] * np.cos(0.75 * x[i])) * np.cos(1.25 * x[i] * np.sin(0.65 * x[i])) * 
                       np.exp(-((x[i] + 1.9)**2 / 6.5)) * scale_factor)
            
        # Polynomial component with fractal-like behavior and higher-order interactions
        poly = 0
        for i in range(self.dim):
            # Modified polynomial with different coefficients
            coef = 1.0 + 0.15 * np.sin(0.45 * i)
            poly += (coef * (x[i]**7 - 14*x[i]**5 + 58*x[i]**3 - 38*x[i]) * 
                    np.exp(-((x[i] - 1.9)**2 / 1.8)) + 
                    0.4 * (x[i]**8 - 18*x[i]**6 + 140*x[i]**4 - 380*x[i]**2) * 
                    np.exp(-((x[i] + 1.4)**2 / 4.5)))
            
        # Complex interaction terms with adaptive weights and fractal-like dependencies
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified interaction with different scaling factors
                weight_factor = 1.0 + 0.25 * np.sin(0.25 * (i + j))
                interaction += (weight_factor * 
                               (np.sin(1.4*x[i]) * np.cos(0.6*x[j]) * np.exp(-((x[i] - x[j])**2 / 4.5)) +
                                np.cos(0.7*x[i]) * np.sin(1.2*x[j]) * np.exp(-((x[i] + x[j])**2 / 8.5))) +
                               (np.sin(2.0*x[i]) * np.cos(1.1*x[j]) * np.exp(-((x[i] - 0.4*x[j])**2 / 3.5)) +
                                np.cos(1.7*x[i]) * np.sin(0.8*x[j]) * np.exp(-((x[i] + 0.6*x[j])**2 / 5.5))))
        
        # Add a new component: nested chaotic landscape with self-similar properties
        nested = 0
        for i in range(self.dim):
            nested += (np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * 
                      np.exp(-((x[i] - np.pi/2)**2 / 3.5)) * 
                      np.sin(np.pi * np.sin(x[i])) + 
                      np.sin(1.8 * x[i]) * np.cos(3.5 * x[i]) * 
                      np.exp(-((x[i] + np.pi/3)**2 / 5.5)) * 
                      np.cos(np.pi * np.cos(x[i])))
        
        # Add a new component: ultra-high frequency chaotic modulation with memory effects
        memory = 0
        for i in range(self.dim):
            memory += (np.sin(9.0 * x[i]) * np.cos(14.0 * x[i]) * 
                      np.exp(-((x[i] - 0.9)**2 / 0.4)) * 
                      np.sin(np.pi * np.sin(np.pi * x[i])) + 
                      np.sin(7.0 * x[i]) * np.cos(11.0 * x[i]) * 
                      np.exp(-((x[i] + 0.9)**2 / 0.6)) * 
                      np.cos(np.pi * np.cos(np.pi * x[i])))
        
        # Add a new component: hybrid fractal-gaussian mixture with dimensional coupling
        fractal_gauss = 0
        for i in range(self.dim):
            fractal_gauss += (np.exp(-x[i]**2) * np.sin(4.5 * x[i]) * 
                             np.cos(2.5 * x[i]) * 
                             np.exp(-((x[i] - 0.4)**2 / 1.3)) + 
                             np.exp(-(x[i]**2)/2) * np.sin(6.5 * x[i]) * 
                             np.cos(3.5 * x[i]) * 
                             np.exp(-((x[i] + 0.7)**2 / 1.8)))
        
        # Add a new component: dynamic resonance landscape with time-like dimension coupling
        resonance = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                resonance += (np.sin(2.3 * x[i]) * np.cos(3.3 * x[j]) * 
                             np.exp(-((x[i] - x[j])**2 / 2.5)) + 
                             np.cos(1.6 * x[i]) * np.sin(2.0 * x[j]) * 
                             np.exp(-((x[i] + x[j])**2 / 3.5)))
        
        # Add a new component: modified chaotic landscape with enhanced nonlinearity
        nonlinear = 0
        for i in range(self.dim):
            nonlinear += (np.sin(4.8 * x[i]) * np.cos(7.8 * x[i]) * 
                         np.exp(-((x[i] - 1.1)**2 / 0.7)) * 
                         np.sin(np.pi * np.sin(1.9 * x[i])) + 
                         np.sin(3.3 * x[i]) * np.cos(5.8 * x[i]) * 
                         np.exp(-((x[i] + 1.2)**2 / 1.1)) * 
                         np.cos(np.pi * np.cos(1.4 * x[i])))
        
        # Add a new component: adaptive multimodal with dynamic scaling
        adaptive_multimodal = 0
        for i in range(self.dim):
            adaptive_multimodal += (np.sin(3.8 * x[i]) * np.cos(2.3 * x[i]) * 
                                  np.exp(-((x[i] - 1.9)**2 / 0.9)) * 
                                  (1 + 0.35 * np.sin(0.45 * i)) + 
                                  np.sin(1.4 * x[i]) * np.cos(2.8 * x[i]) * 
                                  np.exp(-((x[i] + 2.4)**2 / 1.4)) * 
                                  (1 + 0.25 * np.cos(0.65 * i)))
        
        # Add a new component: hybrid chaotic-polynomial with memory
        hybrid = 0
        for i in range(self.dim):
            hybrid += (np.sin(x[i]**2) * np.cos(x[i]) * 
                      np.exp(-((x[i] - 0.9)**2 / 0.4)) + 
                      np.cos(x[i]**3) * np.sin(x[i]) * 
                      np.exp(-((x[i] + 0.9)**2 / 0.7)))
        
        # Add a new component: enhanced fractal landscape with self-similarity and dimensionally coupled scaling
        fractal_enhanced = 0
        for i in range(self.dim):
            fractal_enhanced += (np.sin(2.8 * x[i]) * np.cos(3.8 * x[i]) * 
                               np.exp(-((x[i] - 0.9)**2 / 0.5)) * 
                               np.sin(np.pi * np.sin(0.45 * x[i])) + 
                               np.sin(1.8 * x[i]) * np.cos(4.8 * x[i]) * 
                               np.exp(-((x[i] + 0.9)**2 / 0.7)) * 
                               np.cos(np.pi * np.cos(0.25 * x[i])))
        
        # Add a new component: dynamic chaotic field with time-varying parameters
        dynamic = 0
        for i in range(self.dim):
            dynamic += (np.sin(5.8 * x[i]) * np.cos(6.8 * x[i]) * 
                      np.exp(-((x[i] - 0.4)**2 / 0.25)) * 
                      np.sin(np.pi * np.sin(1.4 * x[i])) + 
                      np.sin(4.3 * x[i]) * np.cos(8.3 * x[i]) * 
                      np.exp(-((x[i] + 0.4)**2 / 0.35)) * 
                      np.cos(np.pi * np.cos(1.1 * x[i])))
        
        # Add a new component: multi-scale chaotic modulation with varying amplitudes
        multiscale = 0
        for i in range(self.dim):
            multiscale += (np.sin(7.8 * x[i]) * np.cos(8.8 * x[i]) * 
                          np.exp(-((x[i] - 1.4)**2 / 0.6)) + 
                          np.sin(4.8 * x[i]) * np.cos(5.8 * x[i]) * 
                          np.exp(-((x[i] + 1.4)**2 / 0.8)))
        
        # Combine all components with optimized weights and scaling factors
        return (sphere * 0.015 + 
                multimodal * 0.32 + 
                chaotic * 0.18 + 
                poly * 0.75 + 
                interaction * 0.18 + 
                nested * 0.04 +
                memory * 0.12 +
                fractal_gauss * 0.06 +
                resonance * 0.06 +
                nonlinear * 0.10 +
                adaptive_multimodal * 0.05 +
                hybrid * 0.03 +
                fractal_enhanced * 0.09 +
                dynamic * 0.02 +
                multiscale * 0.04)