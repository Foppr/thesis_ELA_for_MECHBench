import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial terms with chaotic logistic modulation
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Chaotic logistic map component
            logistic_factor = 1.0
            for i in range(5):
                logistic_factor = 4.0 * logistic_factor * (1.0 - logistic_factor)
            
            # Radial polynomial with chaotic weighting
            poly_term = r**6 - 5*r**4 + 10*r**2 - 8
            result += logistic_factor * poly_term * np.exp(-r/3.0)
        
        # Cross-dimensional chaotic coupling with angular dependence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                
                # Chaotic angular coupling using logistic map
                angle = np.arctan2(xj, xi)
                chaotic_angle = 4.0 * angle * (1.0 - angle)
                
                # Dynamic coupling with fractal-like behavior
                coupling = np.sin(3.0 * xi) * np.cos(3.0 * xj) * np.exp(-((xi-xj)**2)/5.0)
                result += 0.8 * coupling * (1.0 + 0.3 * np.sin(chaotic_angle))
        
        # Multi-scale chaotic radial terms with dynamic scaling
        for i in range(1, 8):
            freq = i * (1.2 + 0.4 * np.sin(r / 2.0))
            amp = 1.0 + 0.5 * np.cos(i * r / 3.0)
            
            # Chaotic modulation using logistic map
            chaotic_mod = 1.0
            for k in range(3):
                chaotic_mod = 4.0 * chaotic_mod * (1.0 - chaotic_mod)
                
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/4.0) * chaotic_mod
        
        # High-order polynomial with chaotic angular modulation
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**7 - 4*xi**5 + 6*xi**3 - 4*xi
            angle_mod = 1.0 + 0.4 * np.sin(xi / 2.0) * np.cos(xi / 3.0)
            
            # Chaotic component for angular modulation
            chaotic_ang = 1.0
            for k in range(4):
                chaotic_ang = 4.0 * chaotic_ang * (1.0 - chaotic_ang)
                
            result += angle_mod * poly_term * np.exp(-abs(xi)/3.5) * chaotic_ang
        
        # Dynamic scaling with chaotic logistic factor
        dynamic_factor = 1.0 + 0.6 * np.sin(r / 2.0) * np.cos(r / 4.0)
        # Add chaotic component to dynamic factor
        chaotic_dynamic = 1.0
        for k in range(3):
            chaotic_dynamic = 4.0 * chaotic_dynamic * (1.0 - chaotic_dynamic)
        result *= dynamic_factor * chaotic_dynamic
        
        # Fractal-like coupling with chaotic frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                
                # Chaotic frequency modulation
                freq_mod = 1.0 + 0.5 * np.sin(xi + xj)
                chaotic_freq = 1.0
                for k in range(2):
                    chaotic_freq = 4.0 * chaotic_freq * (1.0 - chaotic_freq)
                
                fractal_coupling = np.exp(-abs(xi-xj)/3.0) * np.sin(freq_mod * (xi+xj)) * np.cos(chaotic_freq * (xi-xj))
                result += 0.7 * fractal_coupling
        
        # Additional chaotic radial terms with multi-scale interactions
        for i in range(1, 12):
            # Chaotic amplitude modulation
            amp_mod = 1.0
            for k in range(3):
                amp_mod = 4.0 * amp_mod * (1.0 - amp_mod)
                
            freq = i * (1.5 + 0.3 * np.sin(r / 3.0))
            amp = 1.2 + 0.4 * np.cos(i * r / 4.0) * amp_mod
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/5.0)
        
        # Enhanced chaotic angular coupling with polynomial weighting
        for i in range(self.dim):
            xi = x[i]
            poly_weight = xi**4 - 2*xi**2 + 1
            
            # Chaotic component for weighting
            chaotic_weight = 1.0
            for k in range(5):
                chaotic_weight = 4.0 * chaotic_weight * (1.0 - chaotic_weight)
                
            result += poly_weight * np.sin(xi) * np.exp(-abs(xi)/4.0) * chaotic_weight
        
        # Final chaotic scaling factor
        final_chaos = 1.0
        for k in range(4):
            final_chaos = 4.0 * final_chaos * (1.0 - final_chaos)
            
        result *= final_chaos
        
        return result